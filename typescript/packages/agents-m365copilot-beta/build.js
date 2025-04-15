import esbuild from "esbuild";

esbuild
	.build({
		entryPoints: ["./agentsM365CopilotBetaServiceClient.ts"], // Adjust to the main entry file of the package
		bundle: true,
		outfile: "./agentsM365CopilotBetaServiceClient.js",
		platform: "node",
		format: "esm",
		external: ["@microsoft/kiota-authentication-azure", "@microsoft/kiota-bundle"], // Exclude other dependencies
		plugins: [],
	})
	.catch(() => process.exit(1));
