using Microsoft.Kiota.Abstractions.Serialization;

namespace Microsoft.Agents.M365Copilot.Core.Extensions;

/// <summary>
/// Extension helpers for the <see cref="IParseNode"/>
/// </summary>
public static class ParseNodeExtensions
{
    internal static string GetErrorMessage(this IParseNode responseParseNode)
    {
        var errorParseNode = responseParseNode.GetChildNode("error");
        // concatenate the error code and message
        var errorCode = errorParseNode?.GetChildNode("code")?.GetStringValue();
        var errorMessage = errorParseNode?.GetChildNode("message")?.GetStringValue();
        return (string.IsNullOrEmpty(errorCode), string.IsNullOrEmpty(errorMessage)) switch
        {
            (true, true) => null,
            (true, false) => errorMessage,
            (false, true) => errorCode,
            // both error code and message are not null or empty
            // return the error code and message concatenated with a colon
            (false, false) => $"{errorCode} : {errorMessage}"
        };
    }
}
