using Azure.Identity;
using Microsoft.Agents.M365Copilot.Sample;
using Microsoft.Agents.M365Copilot;
using Microsoft.Agents.M365Copilot.Copilot.Retrieval;
using Microsoft.Agents.M365Copilot.Models;
using Microsoft.Extensions.Configuration;

var environment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT") ?? "development";
var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile($"appsettings.{environment}.json", optional: false)
    .Build();

var authConfig = configuration.GetSection("Authentication").Get<AuthConfig>() ?? throw new InvalidOperationException("Authentication configuration is missing or invalid.");

string[] scopes = [
    "Files.Read.All",
    "Sites.Read.All"
];

if (authConfig == null)
{
    throw new InvalidOperationException("Authentication configuration is null.");
}

if (string.IsNullOrEmpty(authConfig.ClientId) || string.IsNullOrEmpty(authConfig.TenantId))
{
    throw new InvalidOperationException("ClientId or TenantId is not set in the configuration.");
}

var deviceCodeCredentialOptions = new DeviceCodeCredentialOptions
{
    ClientId = authConfig.ClientId,
    TenantId = authConfig.TenantId,
    DeviceCodeCallback = (deviceCodeInfo, cancellationToken) =>
    {
        Console.WriteLine(deviceCodeInfo.Message);
        return Task.CompletedTask;
    }
};

var credential = new DeviceCodeCredential(deviceCodeCredentialOptions);

// Create the client with explicit base URL
AgentsM365CopilotServiceClient copilotClient = new AgentsM365CopilotServiceClient(credential, scopes);

try
{
    var requestBody = new RetrievalPostRequestBody
    {
        QueryString = "what is the latest in my organization",
        DataSource = RetrievalDataSource.SharePoint,
    };

#pragma warning disable CS0618 // Type or member is obsolete
    var result = await copilotClient.Copilot.Retrieval.PostAsync(requestBody);
#pragma warning restore CS0618 // Type or member is obsolete

    Console.WriteLine($"Retrieval post: {result}");

    if (result != null)
    {
        Console.WriteLine("Retrieval response received successfully");
        Console.WriteLine("\nResults:");
        Console.WriteLine((result.RetrievalHits != null ? result.RetrievalHits.Count : 0).ToString());

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
                    Console.WriteLine($"  SensitivityLabelId: {hit.SensitivityLabel.SensitivityLabelId}");
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
