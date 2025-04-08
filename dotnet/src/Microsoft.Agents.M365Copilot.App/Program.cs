using Azure.Identity;
using Microsoft.Agents.M365Copilot.Beta;
using Microsoft.Agents.M365Copilot.Beta.Copilot.Retrieval;

string[] scopes = [
    "Files.Read.All",
    "Sites.Read.All"
];

var clientId = "YOUR_CLIENT_ID";
var tenantId = "YOUR_TENANT_ID";

var deviceCodeCredentialOptions = new DeviceCodeCredentialOptions
{
    ClientId = clientId,
    TenantId = tenantId,
    DeviceCodeCallback = (deviceCodeInfo, cancellationToken) =>
    {
        Console.WriteLine(deviceCodeInfo.Message);
        return Task.CompletedTask;
    }
};

var credential = new DeviceCodeCredential(deviceCodeCredentialOptions);

// Create the client with explicit base URL
var baseUrl = "https://graph.microsoft.com/beta";
AgentsCopilotServiceClient copilotClient = new AgentsCopilotServiceClient(credential, scopes, baseUrl);

try
{
    var requestBody = new RetrievalPostRequestBody
    {
        QueryString = "what is the latest in my organization"
    };

#pragma warning disable CS0618 // Type or member is obsolete
    var result = await copilotClient.Copilot.Retrieval.PostAsync(requestBody);
#pragma warning restore CS0618 // Type or member is obsolete

    Console.WriteLine($"Retrieval post: {result}");

    if (result != null)
    {
        Console.WriteLine("Retrieval response received successfully");
        Console.WriteLine("\nResults:");
        Console.WriteLine(result.RetrievalHits.Count.ToString());

        if (result.RetrievalHits != null)
        {
            foreach (var hit in result.RetrievalHits)
            {
                Console.WriteLine("\n---");
                Console.WriteLine($"Web URL: {hit.WebUrl}");
                Console.WriteLine($"Resource Type: {hit.ResourceType}");

                if (hit.Extracts != null && hit.Extracts.Any())
                {
                    Console.WriteLine("\nExtracts:");
                    foreach (var extract in hit.Extracts)
                    {
                        Console.WriteLine($"  {extract.Text}");
                    }
                }

                if (hit.SensitivityLabel != null)
                {
                    Console.WriteLine("\nSensitivity Label:");
                    Console.WriteLine($"  Display Name: {hit.SensitivityLabel.DisplayName}");
                    Console.WriteLine($"  Tooltip: {hit.SensitivityLabel.Tooltip}");
                    Console.WriteLine($"  Priority: {hit.SensitivityLabel.Priority}");
                    Console.WriteLine($"  Color: {hit.SensitivityLabel.Color}");
                    if (hit.SensitivityLabel.IsEncrypted.HasValue)
                    {
                        Console.WriteLine($"  Is Encrypted: {hit.SensitivityLabel.IsEncrypted.Value}");
                    }
                }
            }
        }
        else
        {
            Console.WriteLine("No retrieval hits found in the response");
        }
    }
}
catch (Exception ex)
{
    Console.WriteLine($"Error making retrieval request: {ex.Message}");
    Console.Error.WriteLine(ex);
}