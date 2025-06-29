// <auto-generated/>
#pragma warning disable CS0618
using Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.Messages;
using Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.MicrosoftGraphCopilotChat;
using Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.MicrosoftGraphCopilotChatOverStream;
using Microsoft.Agents.M365Copilot.Beta.Models.ODataErrors;
using Microsoft.Agents.M365Copilot.Beta.Models;
using Microsoft.Kiota.Abstractions.Extensions;
using Microsoft.Kiota.Abstractions.Serialization;
using Microsoft.Kiota.Abstractions;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
using System.Threading;
using System;
namespace Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item
{
    /// <summary>
    /// Provides operations to manage the conversations property of the microsoft.graph.copilotRoot entity.
    /// </summary>
    [global::System.CodeDom.Compiler.GeneratedCode("Kiota", "1.0.0")]
    public partial class CopilotConversationItemRequestBuilder : BaseRequestBuilder
    {
        /// <summary>Provides operations to manage the messages property of the microsoft.graph.copilotConversation entity.</summary>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
        public global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.Messages.MessagesRequestBuilder Messages
        {
            get => new global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.Messages.MessagesRequestBuilder(PathParameters, RequestAdapter);
        }
        /// <summary>Provides operations to call the chat method.</summary>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
        public global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.MicrosoftGraphCopilotChat.MicrosoftGraphCopilotChatRequestBuilder MicrosoftGraphCopilotChat
        {
            get => new global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.MicrosoftGraphCopilotChat.MicrosoftGraphCopilotChatRequestBuilder(PathParameters, RequestAdapter);
        }
        /// <summary>Provides operations to call the chatOverStream method.</summary>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
        public global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.MicrosoftGraphCopilotChatOverStream.MicrosoftGraphCopilotChatOverStreamRequestBuilder MicrosoftGraphCopilotChatOverStream
        {
            get => new global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.MicrosoftGraphCopilotChatOverStream.MicrosoftGraphCopilotChatOverStreamRequestBuilder(PathParameters, RequestAdapter);
        }
        /// <summary>
        /// Instantiates a new <see cref="global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder"/> and sets the default values.
        /// </summary>
        /// <param name="pathParameters">Path parameters for the request</param>
        /// <param name="requestAdapter">The request adapter to use to execute the requests.</param>
        public CopilotConversationItemRequestBuilder(Dictionary<string, object> pathParameters, IRequestAdapter requestAdapter) : base(requestAdapter, "{+baseurl}/copilot/conversations/{copilotConversation%2Did}{?%24expand,%24select}", pathParameters)
        {
        }
        /// <summary>
        /// Instantiates a new <see cref="global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder"/> and sets the default values.
        /// </summary>
        /// <param name="rawUrl">The raw URL to use for the request builder.</param>
        /// <param name="requestAdapter">The request adapter to use to execute the requests.</param>
        public CopilotConversationItemRequestBuilder(string rawUrl, IRequestAdapter requestAdapter) : base(requestAdapter, "{+baseurl}/copilot/conversations/{copilotConversation%2Did}{?%24expand,%24select}", rawUrl)
        {
        }
        /// <summary>
        /// Delete navigation property conversations for copilot
        /// </summary>
        /// <param name="cancellationToken">Cancellation token to use when cancelling requests</param>
        /// <param name="requestConfiguration">Configuration for the request such as headers, query parameters, and middleware options.</param>
        /// <exception cref="global::Microsoft.Agents.M365Copilot.Beta.Models.ODataErrors.ODataError">When receiving a 4XX or 5XX status code</exception>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public async Task DeleteAsync(Action<RequestConfiguration<DefaultQueryParameters>>? requestConfiguration = default, CancellationToken cancellationToken = default)
        {
#nullable restore
#else
        public async Task DeleteAsync(Action<RequestConfiguration<DefaultQueryParameters>> requestConfiguration = default, CancellationToken cancellationToken = default)
        {
#endif
            var requestInfo = ToDeleteRequestInformation(requestConfiguration);
            var errorMapping = new Dictionary<string, ParsableFactory<IParsable>>
            {
                { "XXX", global::Microsoft.Agents.M365Copilot.Beta.Models.ODataErrors.ODataError.CreateFromDiscriminatorValue },
            };
            await RequestAdapter.SendNoContentAsync(requestInfo, errorMapping, cancellationToken).ConfigureAwait(false);
        }
        /// <summary>
        /// The users conversations with Copilot Chat.
        /// </summary>
        /// <returns>A <see cref="global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation"/></returns>
        /// <param name="cancellationToken">Cancellation token to use when cancelling requests</param>
        /// <param name="requestConfiguration">Configuration for the request such as headers, query parameters, and middleware options.</param>
        /// <exception cref="global::Microsoft.Agents.M365Copilot.Beta.Models.ODataErrors.ODataError">When receiving a 4XX or 5XX status code</exception>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public async Task<global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation?> GetAsync(Action<RequestConfiguration<global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder.CopilotConversationItemRequestBuilderGetQueryParameters>>? requestConfiguration = default, CancellationToken cancellationToken = default)
        {
#nullable restore
#else
        public async Task<global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation> GetAsync(Action<RequestConfiguration<global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder.CopilotConversationItemRequestBuilderGetQueryParameters>> requestConfiguration = default, CancellationToken cancellationToken = default)
        {
#endif
            var requestInfo = ToGetRequestInformation(requestConfiguration);
            var errorMapping = new Dictionary<string, ParsableFactory<IParsable>>
            {
                { "XXX", global::Microsoft.Agents.M365Copilot.Beta.Models.ODataErrors.ODataError.CreateFromDiscriminatorValue },
            };
            return await RequestAdapter.SendAsync<global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation>(requestInfo, global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation.CreateFromDiscriminatorValue, errorMapping, cancellationToken).ConfigureAwait(false);
        }
        /// <summary>
        /// Update the navigation property conversations in copilot
        /// </summary>
        /// <returns>A <see cref="global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation"/></returns>
        /// <param name="body">The request body</param>
        /// <param name="cancellationToken">Cancellation token to use when cancelling requests</param>
        /// <param name="requestConfiguration">Configuration for the request such as headers, query parameters, and middleware options.</param>
        /// <exception cref="global::Microsoft.Agents.M365Copilot.Beta.Models.ODataErrors.ODataError">When receiving a 4XX or 5XX status code</exception>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public async Task<global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation?> PatchAsync(global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation body, Action<RequestConfiguration<DefaultQueryParameters>>? requestConfiguration = default, CancellationToken cancellationToken = default)
        {
#nullable restore
#else
        public async Task<global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation> PatchAsync(global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation body, Action<RequestConfiguration<DefaultQueryParameters>> requestConfiguration = default, CancellationToken cancellationToken = default)
        {
#endif
            _ = body ?? throw new ArgumentNullException(nameof(body));
            var requestInfo = ToPatchRequestInformation(body, requestConfiguration);
            var errorMapping = new Dictionary<string, ParsableFactory<IParsable>>
            {
                { "XXX", global::Microsoft.Agents.M365Copilot.Beta.Models.ODataErrors.ODataError.CreateFromDiscriminatorValue },
            };
            return await RequestAdapter.SendAsync<global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation>(requestInfo, global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation.CreateFromDiscriminatorValue, errorMapping, cancellationToken).ConfigureAwait(false);
        }
        /// <summary>
        /// Delete navigation property conversations for copilot
        /// </summary>
        /// <returns>A <see cref="RequestInformation"/></returns>
        /// <param name="requestConfiguration">Configuration for the request such as headers, query parameters, and middleware options.</param>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public RequestInformation ToDeleteRequestInformation(Action<RequestConfiguration<DefaultQueryParameters>>? requestConfiguration = default)
        {
#nullable restore
#else
        public RequestInformation ToDeleteRequestInformation(Action<RequestConfiguration<DefaultQueryParameters>> requestConfiguration = default)
        {
#endif
            var requestInfo = new RequestInformation(Method.DELETE, UrlTemplate, PathParameters);
            requestInfo.Configure(requestConfiguration);
            return requestInfo;
        }
        /// <summary>
        /// The users conversations with Copilot Chat.
        /// </summary>
        /// <returns>A <see cref="RequestInformation"/></returns>
        /// <param name="requestConfiguration">Configuration for the request such as headers, query parameters, and middleware options.</param>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public RequestInformation ToGetRequestInformation(Action<RequestConfiguration<global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder.CopilotConversationItemRequestBuilderGetQueryParameters>>? requestConfiguration = default)
        {
#nullable restore
#else
        public RequestInformation ToGetRequestInformation(Action<RequestConfiguration<global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder.CopilotConversationItemRequestBuilderGetQueryParameters>> requestConfiguration = default)
        {
#endif
            var requestInfo = new RequestInformation(Method.GET, UrlTemplate, PathParameters);
            requestInfo.Configure(requestConfiguration);
            requestInfo.Headers.TryAdd("Accept", "application/json");
            return requestInfo;
        }
        /// <summary>
        /// Update the navigation property conversations in copilot
        /// </summary>
        /// <returns>A <see cref="RequestInformation"/></returns>
        /// <param name="body">The request body</param>
        /// <param name="requestConfiguration">Configuration for the request such as headers, query parameters, and middleware options.</param>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
        public RequestInformation ToPatchRequestInformation(global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation body, Action<RequestConfiguration<DefaultQueryParameters>>? requestConfiguration = default)
        {
#nullable restore
#else
        public RequestInformation ToPatchRequestInformation(global::Microsoft.Agents.M365Copilot.Beta.Models.CopilotConversation body, Action<RequestConfiguration<DefaultQueryParameters>> requestConfiguration = default)
        {
#endif
            _ = body ?? throw new ArgumentNullException(nameof(body));
            var requestInfo = new RequestInformation(Method.PATCH, UrlTemplate, PathParameters);
            requestInfo.Configure(requestConfiguration);
            requestInfo.Headers.TryAdd("Accept", "application/json");
            requestInfo.SetContentFromParsable(RequestAdapter, "application/json", body);
            return requestInfo;
        }
        /// <summary>
        /// Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        /// </summary>
        /// <returns>A <see cref="global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder"/></returns>
        /// <param name="rawUrl">The raw URL to use for the request builder.</param>
        [Obsolete(" as of 2025-03/PrivatePreview:copilotChatPrivatePreview1 on 2025-03-27 and will be removed 2025-08-28")]
        public global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder WithUrl(string rawUrl)
        {
            return new global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder(rawUrl, RequestAdapter);
        }
        /// <summary>
        /// Configuration for the request such as headers, query parameters, and middleware options.
        /// </summary>
        [Obsolete("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.")]
        [global::System.CodeDom.Compiler.GeneratedCode("Kiota", "1.0.0")]
        public partial class CopilotConversationItemRequestBuilderDeleteRequestConfiguration : RequestConfiguration<DefaultQueryParameters>
        {
        }
        /// <summary>
        /// The users conversations with Copilot Chat.
        /// </summary>
        [global::System.CodeDom.Compiler.GeneratedCode("Kiota", "1.0.0")]
        public partial class CopilotConversationItemRequestBuilderGetQueryParameters 
        {
            /// <summary>Expand related entities</summary>
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
            [QueryParameter("%24expand")]
            public string[]? Expand { get; set; }
#nullable restore
#else
            [QueryParameter("%24expand")]
            public string[] Expand { get; set; }
#endif
            /// <summary>Select properties to be returned</summary>
#if NETSTANDARD2_1_OR_GREATER || NETCOREAPP3_1_OR_GREATER
#nullable enable
            [QueryParameter("%24select")]
            public string[]? Select { get; set; }
#nullable restore
#else
            [QueryParameter("%24select")]
            public string[] Select { get; set; }
#endif
        }
        /// <summary>
        /// Configuration for the request such as headers, query parameters, and middleware options.
        /// </summary>
        [Obsolete("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.")]
        [global::System.CodeDom.Compiler.GeneratedCode("Kiota", "1.0.0")]
        public partial class CopilotConversationItemRequestBuilderGetRequestConfiguration : RequestConfiguration<global::Microsoft.Agents.M365Copilot.Beta.Copilot.Conversations.Item.CopilotConversationItemRequestBuilder.CopilotConversationItemRequestBuilderGetQueryParameters>
        {
        }
        /// <summary>
        /// Configuration for the request such as headers, query parameters, and middleware options.
        /// </summary>
        [Obsolete("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.")]
        [global::System.CodeDom.Compiler.GeneratedCode("Kiota", "1.0.0")]
        public partial class CopilotConversationItemRequestBuilderPatchRequestConfiguration : RequestConfiguration<DefaultQueryParameters>
        {
        }
    }
}
#pragma warning restore CS0618
