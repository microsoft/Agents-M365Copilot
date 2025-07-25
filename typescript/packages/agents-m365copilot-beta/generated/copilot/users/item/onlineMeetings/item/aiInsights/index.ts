/* tslint:disable */
/* eslint-disable */
// Generated by Microsoft Kiota
// @ts-ignore
import { createCallAiInsightCollectionResponseFromDiscriminatorValue, createCallAiInsightFromDiscriminatorValue, serializeCallAiInsight, type CallAiInsight, type CallAiInsightCollectionResponse } from '../../../../../../models/index.js';
// @ts-ignore
import { createODataErrorFromDiscriminatorValue, type ODataError } from '../../../../../../models/oDataErrors/index.js';
// @ts-ignore
import { CountRequestBuilderRequestsMetadata, type CountRequestBuilder } from './count/index.js';
// @ts-ignore
import { CallAiInsightItemRequestBuilderRequestsMetadata, type CallAiInsightItemRequestBuilder } from './item/index.js';
// @ts-ignore
import { type BaseRequestBuilder, type KeysToExcludeForNavigationMetadata, type NavigationMetadata, type Parsable, type ParsableFactory, type RequestConfiguration, type RequestInformation, type RequestsMetadata } from '@microsoft/kiota-abstractions';

/**
 * Provides operations to manage the aiInsights property of the microsoft.graph.aiOnlineMeeting entity.
 */
export interface AiInsightsRequestBuilder extends BaseRequestBuilder<AiInsightsRequestBuilder> {
    /**
     * Provides operations to count the resources in the collection.
     */
    get count(): CountRequestBuilder;
    /**
     * Provides operations to manage the aiInsights property of the microsoft.graph.aiOnlineMeeting entity.
     * @param callAiInsightId The unique identifier of callAiInsight
     * @returns {CallAiInsightItemRequestBuilder}
     */
     byCallAiInsightId(callAiInsightId: string) : CallAiInsightItemRequestBuilder;
    /**
     * Get the list of callAiInsight objects associated with an onlineMeeting.
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {Promise<CallAiInsightCollectionResponse>}
     * @throws {ODataError} error when the service returns a 4XX or 5XX status code
     * @see {@link https://learn.microsoft.com/graph/api/onlinemeeting-list-aiinsights?view=graph-rest-beta|Find more info here}
     */
     get(requestConfiguration?: RequestConfiguration<AiInsightsRequestBuilderGetQueryParameters> | undefined) : Promise<CallAiInsightCollectionResponse | undefined>;
    /**
     * Create new navigation property to aiInsights for copilot
     * @param body The request body
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {Promise<CallAiInsight>}
     * @throws {ODataError} error when the service returns a 4XX or 5XX status code
     */
     post(body: CallAiInsight, requestConfiguration?: RequestConfiguration<object> | undefined) : Promise<CallAiInsight | undefined>;
    /**
     * Get the list of callAiInsight objects associated with an onlineMeeting.
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {RequestInformation}
     */
     toGetRequestInformation(requestConfiguration?: RequestConfiguration<AiInsightsRequestBuilderGetQueryParameters> | undefined) : RequestInformation;
    /**
     * Create new navigation property to aiInsights for copilot
     * @param body The request body
     * @param requestConfiguration Configuration for the request such as headers, query parameters, and middleware options.
     * @returns {RequestInformation}
     */
     toPostRequestInformation(body: CallAiInsight, requestConfiguration?: RequestConfiguration<object> | undefined) : RequestInformation;
}
/**
 * Get the list of callAiInsight objects associated with an onlineMeeting.
 */
export interface AiInsightsRequestBuilderGetQueryParameters {
    /**
     * Include count of items
     */
    count?: boolean;
    /**
     * Expand related entities
     */
    expand?: string[];
    /**
     * Filter items by property values
     */
    filter?: string;
    /**
     * Order items by property values
     */
    orderby?: string[];
    /**
     * Search items by search phrases
     */
    search?: string;
    /**
     * Select properties to be returned
     */
    select?: string[];
    /**
     * Skip the first n items
     */
    skip?: number;
    /**
     * Show only the first n items
     */
    top?: number;
}
/**
 * Uri template for the request builder.
 */
export const AiInsightsRequestBuilderUriTemplate = "{+baseurl}/copilot/users/{aiUser%2Did}/onlineMeetings/{aiOnlineMeeting%2Did}/aiInsights{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}";
/**
 * Mapper for query parameters from symbol name to serialization name represented as a constant.
 */
const AiInsightsRequestBuilderGetQueryParametersMapper: Record<string, string> = {
    "count": "%24count",
    "expand": "%24expand",
    "filter": "%24filter",
    "orderby": "%24orderby",
    "search": "%24search",
    "select": "%24select",
    "skip": "%24skip",
    "top": "%24top",
};
/**
 * Metadata for all the navigation properties in the request builder.
 */
export const AiInsightsRequestBuilderNavigationMetadata: Record<Exclude<keyof AiInsightsRequestBuilder, KeysToExcludeForNavigationMetadata>, NavigationMetadata> = {
    byCallAiInsightId: {
        requestsMetadata: CallAiInsightItemRequestBuilderRequestsMetadata,
        pathParametersMappings: ["callAiInsight%2Did"],
    },
    count: {
        requestsMetadata: CountRequestBuilderRequestsMetadata,
    },
};
/**
 * Metadata for all the requests in the request builder.
 */
export const AiInsightsRequestBuilderRequestsMetadata: RequestsMetadata = {
    get: {
        uriTemplate: AiInsightsRequestBuilderUriTemplate,
        responseBodyContentType: "application/json",
        errorMappings: {
            XXX: createODataErrorFromDiscriminatorValue as ParsableFactory<Parsable>,
        },
        adapterMethodName: "send",
        responseBodyFactory:  createCallAiInsightCollectionResponseFromDiscriminatorValue,
        queryParametersMapper: AiInsightsRequestBuilderGetQueryParametersMapper,
    },
    post: {
        uriTemplate: AiInsightsRequestBuilderUriTemplate,
        responseBodyContentType: "application/json",
        errorMappings: {
            XXX: createODataErrorFromDiscriminatorValue as ParsableFactory<Parsable>,
        },
        adapterMethodName: "send",
        responseBodyFactory:  createCallAiInsightFromDiscriminatorValue,
        requestBodyContentType: "application/json",
        requestBodySerializer: serializeCallAiInsight,
        requestInformationContentSetMethod: "setContentFromParsable",
    },
};
/* tslint:enable */
/* eslint-enable */
