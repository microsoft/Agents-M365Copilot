namespace Microsoft.Agents.M365Copilot.Core.Requests.Content
{
    using System.Collections.Generic;

    internal class KeyedBatchResponseContent
    {
        internal readonly HashSet<string> Keys;
        internal readonly BatchResponseContent Response;

        public KeyedBatchResponseContent(HashSet<string> keys, BatchResponseContent response)
        {
            Keys = keys;
            Response = response;
        }
    }
}
