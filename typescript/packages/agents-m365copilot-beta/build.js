import esbuild from "esbuild";

// Node specific bundle
esbuild
	.build({
		entryPoints: ["./generated/baseAgentsM365CopilotBetaServiceClient.ts"], // Adjust to the main entry file of the package
		bundle: true,
		outfile: "./dist/index.node.js",
		platform: "node",
		format: "esm",
		external: ["@microsoft/kiota-authentication-azure", "@microsoft/kiota-bundle"], // Exclude other dependencies
		minify: true
	})
	.catch(() => process.exit(1));

// Browser specific bundle
esbuild
	.build({
		entryPoints: ["./generated/baseAgentsM365CopilotBetaServiceClient.ts"], // Adjust to the main entry file of the package
		bundle: true,
		outfile: "./dist/index.browser.js",
		platform: "browser",
		format: "esm",
		external: ["@microsoft/kiota-authentication-azure", "@microsoft/kiota-bundle"], // Exclude other dependencies
		minify: true
	})
	.catch(() => process.exit(1));
