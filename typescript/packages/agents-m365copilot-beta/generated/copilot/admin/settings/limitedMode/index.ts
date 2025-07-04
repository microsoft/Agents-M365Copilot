/* tslint:disable */
/* eslint-disable */
// Generated by Microsoft Kiota
// @ts-ignore
import { createCopilotAdminLimitedModeFromDiscriminatorValue, serializeCopilotAdminLimitedMode, type CopilotAdminLimitedMode } from '../../../../models/index.js';
// @ts-ignore
import { createODataErrorFromDiscriminatorValue, type ODataError } from '../../../../models/oDataErrors/index.js';
// @ts-ignore
import { type BaseRequestBuilder, type Parsable, type ParsableFactory, type RequestConfiguration, type RequestInformation, type RequestsMetadata } from '@microsoft/kiota-abstractions';

/**
 * Provides operations to manage the limitedMode property of the microsoft.graph.copilotAdminSetting entity.
 */
export interface LimitedModeRequestBuilder extends BaseRequestBuilder<LimitedModeRequestBuilder> {
    /**
     * Delete navigation property limitedMode for copilot
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @throws {ODataError} error when the service returns a 4XX or 5XX status code
     */
     delete(requestConfiguration?: RequestConfiguration<object> | undefined) : Promise<void>;
    /**
     * Read the properties and relationships of a copilotAdminLimitedMode object.
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {Promise<CopilotAdminLimitedMode>}
     * @throws {ODataError} error when the service returns a 4XX or 5XX status code
     * @see {@link https://learn.microsoft.com/graph/api/copilotadminlimitedmode-get?view=graph-rest-beta|Find more info here}
     */
     get(requestConfiguration?: RequestConfiguration<LimitedModeRequestBuilderGetQueryParameters> | undefined) : Promise<CopilotAdminLimitedMode | undefined>;
    /**
     * Update the properties of a copilotAdminLimitedMode object.
     * @param body The request body
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {Promise<CopilotAdminLimitedMode>}
     * @throws {ODataError} error when the service returns a 4XX or 5XX status code
     * @see {@link https://learn.microsoft.com/graph/api/copilotadminlimitedmode-update?view=graph-rest-beta|Find more info here}
     */
     patch(body: CopilotAdminLimitedMode, requestConfiguration?: RequestConfiguration<object> | undefined) : Promise<CopilotAdminLimitedMode | undefined>;
    /**
     * Delete navigation property limitedMode for copilot
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {RequestInformation}
     */
     toDeleteRequestInformation(requestConfiguration?: RequestConfiguration<object> | undefined) : RequestInformation;
    /**
     * Read the properties and relationships of a copilotAdminLimitedMode object.
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {RequestInformation}
     */
     toGetRequestInformation(requestConfiguration?: RequestConfiguration<LimitedModeRequestBuilderGetQueryParameters> | undefined) : RequestInformation;
    /**
     * Update the properties of a copilotAdminLimitedMode object.
     * @param body The request body
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {RequestInformation}
     */
     toPatchRequestInformation(body: CopilotAdminLimitedMode, requestConfiguration?: RequestConfiguration<object> | undefined) : RequestInformation;
}
/**
 * Read the properties and relationships of a copilotAdminLimitedMode object.
 */
export interface LimitedModeRequestBuilderGetQueryParameters {
    /**
     * Expand related entities
     */
    expand?: string[];
    /**
     * Select properties to be returned
     */
    select?: string[];
}
/**
 * Uri template for the request builder.
 */
export const LimitedModeRequestBuilderUriTemplate = "{+baseurl}/copilot/admin/settings/limitedMode{?%24expand,%24select}";
/**
 * Mapper for query parameters from symbol name to serialization name represented as a constant.
 */
const LimitedModeRequestBuilderGetQueryParametersMapper: Record<string, string> = {
    "expand": "%24expand",
    "select": "%24select",
};
/**
 * Metadata for all the requests in the request builder.
 */
export const LimitedModeRequestBuilderRequestsMetadata: RequestsMetadata = {
    delete: {
        uriTemplate: LimitedModeRequestBuilderUriTemplate,
        responseBodyContentType: "application/json",
        errorMappings: {
            XXX: createODataErrorFromDiscriminatorValue as ParsableFactory<Parsable>,
        },
        adapterMethodName: "sendNoResponseContent",
    },
    get: {
        uriTemplate: LimitedModeRequestBuilderUriTemplate,
        responseBodyContentType: "application/json",
        errorMappings: {
            XXX: createODataErrorFromDiscriminatorValue as ParsableFactory<Parsable>,
        },
        adapterMethodName: "send",
        responseBodyFactory:  createCopilotAdminLimitedModeFromDiscriminatorValue,
        queryParametersMapper: LimitedModeRequestBuilderGetQueryParametersMapper,
    },
    patch: {
        uriTemplate: LimitedModeRequestBuilderUriTemplate,
        responseBodyContentType: "application/json",
        errorMappings: {
            XXX: createODataErrorFromDiscriminatorValue as ParsableFactory<Parsable>,
        },
        adapterMethodName: "send",
        responseBodyFactory:  createCopilotAdminLimitedModeFromDiscriminatorValue,
        requestBodyContentType: "application/json",
        requestBodySerializer: serializeCopilotAdminLimitedMode,
        requestInformationContentSetMethod: "setContentFromParsable",
    },
};
/* tslint:enable */
/* eslint-enable */
