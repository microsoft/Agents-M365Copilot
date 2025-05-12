# Getting the latest Copilot Open API files

**NOTE**

> This is experimental to validate the copilot endpoints for initial generations when building the SDKs. After the Copilot endpoints are in public mode, this mode of generating open api files will be deprecated.

## Get the latest workloads from the AGS repo

You need to have the latest workloads from the internal AGS repo.

1. Clone the repository of the AGS Workloads

   ```bash
   git clone https://msazure.visualstudio.com/DefaultCollection/One/_git/AD-AggregatorService-Workloads
   ```

1. Install graph studio by running the command `\.InstallGraphStudio.ps1` from the root of the cloned repository.

   ```bash
   cd AD-AggregatorService-Workloads && \.InstallGraphStudio.ps1
   ```

1. Generate the csdl metadata files. This will prompt a login to your corp account so that you can acquire a token.

   ```bash
   gs validate -t schema
   ```

## Running `hidi` to convert the CSDL to Open API

By now, the graph studio command has generated a `Schemas` folder in the root of the cloned AGS workloads repo.

1. Install `hidi` globally

   ```bash
   dotnet tool install --global Microsoft.OpenApi.Hidi
   ```

1. Download the conversion settings to use for SDK generation from the metadata repository

   ```bash
   Invoke-WebRequest https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/refs/heads/master/conversion-settings/openapi.json -OutFile openapi-settings.json
   ```

1. Run `hidi` to convert the `Schemas/beta-Review.csdl` file into an Open API file called `ccs-beta-openapi.yml`.

   **NOTE**

   > We pass the `--csdl-filter "copilot"` in this scenario to only include paths under the `/copilot` path as the metadata is very large.

   ```bash
   hidi transform --csdl .\Schemas\beta-Review.csdl --output ccs-beta-openapi.yml --settings-path .\openapi-settings.json --version 3.0 --metadata-version "beta" --log-level Information --format yaml --csdl-filter "copilot"
   ```

## Migrating to the public copilot metadata

To start using the public available metadata in https://github.com/microsoftgraph/msgraph-metadata, we need to update the generation pipeline templates to remove the following:

1. Remove this parameter from the setup step and references it has

   https://github.com/microsoftgraph/MSGraph-SDK-Code-Generator/blob/2939a96c644300034dc0c8ba47de63f6fe038102/.azure-pipelines/generation-templates/set-up-for-generation-kiota.yml#L9-L10

1. Drop this step as well as it copies the Open Api file to the expected metadata location

   https://github.com/microsoftgraph/MSGraph-SDK-Code-Generator/blob/2939a96c644300034dc0c8ba47de63f6fe038102/.azure-pipelines/generation-templates/set-up-for-generation-kiota.yml#L28-L41

1. Delete this `openapi` folder as it is no longer used.
