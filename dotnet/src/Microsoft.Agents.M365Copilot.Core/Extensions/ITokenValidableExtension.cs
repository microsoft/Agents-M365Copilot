﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Extensions
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel;
    using System.IdentityModel.Tokens.Jwt;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.Agents.M365Copilot.Core.Models;
    using Microsoft.IdentityModel.Protocols;
    using Microsoft.IdentityModel.Protocols.OpenIdConnect;
    using Microsoft.IdentityModel.Tokens;
    using Microsoft.IdentityModel.Validators;

    /// <summary>
    /// Contains extension methods for <see cref="ITokenValidableExtension"/>
    /// </summary>
    public static class ITokenValidableExtension
    {
        /// <summary>
        /// Validates tokens attached with the notification collection. If the result is false, the notification collection should be discarded.
        /// </summary>
        /// <param name="collection">Collection instance of <see cref="ITokenValidable{T1,T2}"/></param>
        /// <param name="tenantIds">List of tenant ids that notifications might be originating from.</param>
        /// <param name="appIds">List of application id (client ids) that subscriptions have been created from.</param>
        /// <param name="wellKnownUri">Well known URL to get the signing certificates for the tokens.
        /// If you are not using the public cloud you need to pass the value corresponding to your national deployment.</param>
        /// <param name="issuerFormats">Issuer formats for the "aud" claim in the tokens.
        /// If you are not using the public cloud you need to pass the value corresponding to your national deployment.</param>
        /// <exception cref="ArgumentNullException">Thrown when <paramref name="tenantIds"/> or <paramref name="appIds"/> is null or empty</exception>
        /// <returns>Are tokens valid or not.</returns>
        [Obsolete("This method is obsolete. Use the async version instead.")]
        [EditorBrowsable(EditorBrowsableState.Never)]
#pragma warning disable VSTHRD200 // Use "Async" suffix for async methods
        public static async Task<bool> AreTokensValid<T1, T2>(this ITokenValidable<T1, T2> collection, IEnumerable<Guid> tenantIds, IEnumerable<Guid> appIds,
#pragma warning restore VSTHRD200 // Use "Async" suffix for async methods
            string wellKnownUri = "https://login.microsoftonline.com/common/.well-known/openid-configuration",
            IEnumerable<string> issuerFormats = null) where T1 : IEncryptedContentBearer<T2> where T2 : IDecryptableContent
            => await AreTokensValidAsync(collection, tenantIds, appIds, wellKnownUri, issuerFormats).ConfigureAwait(false);
        /// <summary>
        /// Validates tokens attached with the notification collection. If the result is false, the notification collection should be discarded.
        /// </summary>
        /// <param name="collection">Collection instance of <see cref="ITokenValidable{T1,T2}"/></param>
        /// <param name="tenantIds">List of tenant ids that notifications might be originating from.</param>
        /// <param name="appIds">List of application id (client ids) that subscriptions have been created from.</param>
        /// <param name="wellKnownUri">Well known URL to get the signing certificates for the tokens.
        /// If you are not using the public cloud you need to pass the value corresponding to your national deployment.</param>
        /// <param name="issuerFormats">Issuer formats for the "aud" claim in the tokens.
        /// If you are not using the public cloud you need to pass the value corresponding to your national deployment.</param>
        /// <exception cref="ArgumentNullException">Thrown when <paramref name="tenantIds"/> or <paramref name="appIds"/> is null or empty</exception>
        /// <returns>Are tokens valid or not.</returns>
        public static async Task<bool> AreTokensValidAsync<T1, T2>(this ITokenValidable<T1, T2> collection, IEnumerable<Guid> tenantIds, IEnumerable<Guid> appIds,
            string wellKnownUri = "https://login.microsoftonline.com/common/.well-known/openid-configuration",
            IEnumerable<string> issuerFormats = null) where T1 : IEncryptedContentBearer<T2> where T2 : IDecryptableContent
        {
            if ((collection.ValidationTokens == null || !collection.ValidationTokens.Any()) && collection.Value.All(x => x.EncryptedContent == null))
                return true;

            if (tenantIds == null || !tenantIds.Any())
                throw new ArgumentNullException(nameof(tenantIds));
            if (appIds == null || !appIds.Any())
                throw new ArgumentNullException(nameof(appIds));
            if (!(issuerFormats?.Any() ?? false))
                issuerFormats = new string[] { "https://sts.windows.net/{0}/", "https://login.microsoftonline.com/{0}/v2.0" };

            var configurationManager = new ConfigurationManager<OpenIdConnectConfiguration>(wellKnownUri, new OpenIdConnectConfigurationRetriever());
            var openIdConfig = await configurationManager.GetConfigurationAsync().ConfigureAwait(false);
            var handler = new JwtSecurityTokenHandler();
            var appIdsToValidate = appIds.Select(x => x.ToString());
            foreach (var issuerFormat in issuerFormats)
            {
                var issuersToValidate = tenantIds.Select(x => string.Format(issuerFormat, x));
                var result = collection.ValidationTokens.Select(x => IsTokenValid(x, handler, openIdConfig, issuersToValidate, appIdsToValidate))
                            .Aggregate(static (z, y) => z && y);

                if (result)
                    return result;// no need to try the other issuer if this one worked.
            }

            return false;// All issuers failed
        }

        private static bool IsTokenValid(string token, JwtSecurityTokenHandler handler, OpenIdConnectConfiguration openIdConfig, IEnumerable<string> issuersToValidate, IEnumerable<string> appIds)
        {
            try
            {
                var tokenValidationParameters = new TokenValidationParameters
                {
                    ValidateIssuer = true,
                    ValidateAudience = true,
                    ValidateIssuerSigningKey = true,
                    ValidateLifetime = true,
                    ValidIssuers = issuersToValidate,
                    ValidAudiences = appIds,
                    IssuerSigningKeys = openIdConfig.SigningKeys
                };
                tokenValidationParameters.EnableAadSigningKeyIssuerValidation();
                handler.ValidateToken(token, tokenValidationParameters, out _);
            }
            catch
            {
                return false;
            }

            return true;
        }
    }
}
