/* tslint:disable */
/* eslint-disable */
// Generated by Microsoft Kiota
// @ts-ignore
import { createAiOnlineMeetingFromDiscriminatorValue, serializeAiOnlineMeeting, type AiOnlineMeeting } from '../../../../../models/index.js';
// @ts-ignore
import { createODataErrorFromDiscriminatorValue, type ODataError } from '../../../../../models/oDataErrors/index.js';
// @ts-ignore
import { AiInsightsRequestBuilderNavigationMetadata, AiInsightsRequestBuilderRequestsMetadata, type AiInsightsRequestBuilder } from './aiInsights/index.js';
// @ts-ignore
import { type BaseRequestBuilder, type KeysToExcludeForNavigationMetadata, type NavigationMetadata, type Parsable, type ParsableFactory, type RequestConfiguration, type RequestInformation, type RequestsMetadata } from '@microsoft/kiota-abstractions';

/**
 * Provides operations to manage the onlineMeetings property of the microsoft.graph.aiUser entity.
 */
export interface AiOnlineMeetingItemRequestBuilder extends BaseRequestBuilder<AiOnlineMeetingItemRequestBuilder> {
    /**
     * Provides operations to manage the aiInsights property of the microsoft.graph.aiOnlineMeeting entity.
     */
    get aiInsights(): AiInsightsRequestBuilder;
    /**
     * Delete navigation property onlineMeetings for copilot
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @throws {ODataError} error when the service returns a 4XX or 5XX status code
     */
     delete(requestConfiguration?: RequestConfiguration<object> | undefined) : Promise<void>;
    /**
     * Information about an online meeting, including AI insights.
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {Promise<AiOnlineMeeting>}
     * @throws {ODataError} error when the service returns a 4XX or 5XX status code
     */
     get(requestConfiguration?: RequestConfiguration<AiOnlineMeetingItemRequestBuilderGetQueryParameters> | undefined) : Promise<AiOnlineMeeting | undefined>;
    /**
     * Update the navigation property onlineMeetings in copilot
     * @param body The request body
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {Promise<AiOnlineMeeting>}
     * @throws {ODataError} error when the service returns a 4XX or 5XX status code
     */
     patch(body: AiOnlineMeeting, requestConfiguration?: RequestConfiguration<object> | undefined) : Promise<AiOnlineMeeting | undefined>;
    /**
     * Delete navigation property onlineMeetings for copilot
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {RequestInformation}
     */
     toDeleteRequestInformation(requestConfiguration?: RequestConfiguration<object> | undefined) : RequestInformation;
    /**
     * Information about an online meeting, including AI insights.
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {RequestInformation}
     */
     toGetRequestInformation(requestConfiguration?: RequestConfiguration<AiOnlineMeetingItemRequestBuilderGetQueryParameters> | undefined) : RequestInformation;
    /**
     * Update the navigation property onlineMeetings in copilot
     * @param body The request body
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {RequestInformation}
     */
     toPatchRequestInformation(body: AiOnlineMeeting, requestConfiguration?: RequestConfiguration<object> | undefined) : RequestInformation;
}
/**
 * Information about an online meeting, including AI insights.
 */
export interface AiOnlineMeetingItemRequestBuilderGetQueryParameters {
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
export const AiOnlineMeetingItemRequestBuilderUriTemplate = "{+baseurl}/copilot/users/{aiUser%2Did}/onlineMeetings/{aiOnlineMeeting%2Did}{?%24expand,%24select}";
/**
 * Mapper for query parameters from symbol name to serialization name represented as a constant.
 */
const AiOnlineMeetingItemRequestBuilderGetQueryParametersMapper: Record<string, string> = {
    "expand": "%24expand",
    "select": "%24select",
};
/**
 * Metadata for all the navigation properties in the request builder.
 */
export const AiOnlineMeetingItemRequestBuilderNavigationMetadata: Record<Exclude<keyof AiOnlineMeetingItemRequestBuilder, KeysToExcludeForNavigationMetadata>, NavigationMetadata> = {
    aiInsights: {
        requestsMetadata: AiInsightsRequestBuilderRequestsMetadata,
        navigationMetadata: AiInsightsRequestBuilderNavigationMetadata,
    },
};
/**
 * Metadata for all the requests in the request builder.
 */
export const AiOnlineMeetingItemRequestBuilderRequestsMetadata: RequestsMetadata = {
    delete: {
        uriTemplate: AiOnlineMeetingItemRequestBuilderUriTemplate,
        responseBodyContentType: "application/json",
        errorMappings: {
            XXX: createODataErrorFromDiscriminatorValue as ParsableFactory<Parsable>,
        },
        adapterMethodName: "sendNoResponseContent",
    },
    get: {
        uriTemplate: AiOnlineMeetingItemRequestBuilderUriTemplate,
        responseBodyContentType: "application/json",
        errorMappings: {
            XXX: createODataErrorFromDiscriminatorValue as ParsableFactory<Parsable>,
        },
        adapterMethodName: "send",
        responseBodyFactory:  createAiOnlineMeetingFromDiscriminatorValue,
        queryParametersMapper: AiOnlineMeetingItemRequestBuilderGetQueryParametersMapper,
    },
    patch: {
        uriTemplate: AiOnlineMeetingItemRequestBuilderUriTemplate,
        responseBodyContentType: "application/json",
        errorMappings: {
            XXX: createODataErrorFromDiscriminatorValue as ParsableFactory<Parsable>,
        },
        adapterMethodName: "send",
        responseBodyFactory:  createAiOnlineMeetingFromDiscriminatorValue,
        requestBodyContentType: "application/json",
        requestBodySerializer: serializeAiOnlineMeeting,
        requestInformationContentSetMethod: "setContentFromParsable",
    },
};
/* tslint:enable */
/* eslint-enable */
