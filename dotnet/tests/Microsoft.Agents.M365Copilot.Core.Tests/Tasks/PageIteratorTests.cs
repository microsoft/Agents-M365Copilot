﻿// ------------------------------------------------------------------------------
//  Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
// ------------------------------------------------------------------------------

namespace Microsoft.Agents.M365Copilot.Core.Tests.Tasks
{
    using System;
    using System.Collections.Generic;
    using System.Net;
    using System.Net.Http;
    using System.Text;
    using System.Text.Json;
    using System.Threading;
    using System.Threading.Tasks;
    using Microsoft.Agents.M365Copilot.Core.Exceptions;
    using Microsoft.Agents.M365Copilot.Core.Requests;
    using Microsoft.Agents.M365Copilot.Core.Tasks;
    using Microsoft.Agents.M365Copilot.Core.Tests.Mocks;
    using Microsoft.Agents.M365Copilot.Core.Tests.TestModels.ServiceModels;
    using Microsoft.Kiota.Abstractions;
    using Microsoft.Kiota.Abstractions.Authentication;
    using Microsoft.Kiota.Abstractions.Serialization;
    using Microsoft.Kiota.Serialization.Json;
    using Moq;
    using Xunit;

    /**
     Spec https://github.com/microsoftgraph/msgraph-sdk-design/blob/main/tasks/PageIteratorTask.md
    **/
    public class PageIteratorTests
    {
        private PageIterator<TestEventItem, TestEventsResponse> eventPageIterator;
        private Mock<IRequestAdapter> mockRequestAdapter;
        private IBaseClient baseClient;

        public PageIteratorTests()
        {
            this.mockRequestAdapter = new Mock<IRequestAdapter>(MockBehavior.Strict);
            var mockClient = new Mock<IBaseClient>();
            mockClient.SetupGet((client) => client.RequestAdapter).Returns(mockRequestAdapter.Object);
            this.baseClient = mockClient.Object;

        }

        [Fact]
        public void Given_Non_Collection_IParsable_It_Throws_ArgumentException()
        {
            var fakePage = new TestEventItem();// This is an IParsable but is not a collectionResponse

            var exception = Assert.Throws<ArgumentException>(() => PageIterator<TestEventItem, TestEventItem>.CreatePageIterator(baseClient, fakePage, (e) => { return true; }));
            Assert.Equal("The Parsable does not contain a collection property", exception.Message);
        }

        [Fact]
        public void Given_Null_CollectionPage_It_Throws_ArgumentNullException()
        {
            Assert.Throws<ArgumentNullException>(() => PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, null, (e) => { return true; }));
        }

        [Fact]
        public void Given_Null_Async_Delegate_It_Throws_ArgumentNullException()
        {
            Assert.Throws<ArgumentNullException>(() => PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, new TestEventsResponse(), asyncCallback: null));
        }

        [Fact]
        public void Given_Null_Delegate_It_Throws_ArgumentNullException()
        {
            Assert.Throws<ArgumentNullException>(() => PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, new TestEventsResponse(), callback: null));
        }

        [Fact]
        public async Task Given_Concrete_Generated_CollectionPage_It_Iterates_Page_ItemsAsync()
        {
            // Arrange the sample first page
            var inputEventCount = 17;
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>() };
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            var events = new List<TestEventItem>();

            // Act by using callback to populate the collection
            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, (e) =>
            {
                events.Add(e);
                return true;
            });

            Assert.False(eventPageIterator.IsProcessPageItemCallbackAsync);
            await eventPageIterator.IterateAsync();

            // Assert the collection is not empty and has the same numbers
            Assert.NotEmpty(events);
            Assert.Equal(inputEventCount, events.Count);
        }

        [Fact]
        public async Task Given_Concrete_Generated_CollectionPage_It_Stops_Iterating_Page_ItemsAsync()
        {
            // Arrange the sample first page
            var inputEventCount = 10;
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>() };
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            var events = new List<TestEventItem>();

            // Act by using callback to populate the collection but will return false in the middle
            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, (e) =>
            {
                if (e.Subject == "Subject7")
                    return false;

                events.Add(e);
                return true;
            });

            await eventPageIterator.IterateAsync();

            // Assert the collection is not empty and paging was paused
            Assert.Equal(7, events.Count);
            Assert.Equal(PagingState.Paused, eventPageIterator.State);
        }

        [Fact]
        public async Task Given_CollectionPage_It_Stops_Iterating_Across_PagesAsync()
        {
            // Arrange the sample first page
            // Create the 17 events to initialize the original collection page.
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>() };
            var inputEventCount = 17;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            // Create the 5 events to initialize the next collection page.
            var nextPage = new TestEventsResponse() { Value = new List<TestEventItem>() };
            int nextPageEventCount = 5;
            for (int i = 0; i < nextPageEventCount; i++)
            {
                nextPage.Value.Add(new TestEventItem() { Subject = $"Subject for next page events: {i}" });
            }

            // Create the CancellationTokenSource to test the cancellation of paging in the delegate.
            var cancellationTokenSource = new CancellationTokenSource();
            var pagingToken = cancellationTokenSource.Token;

            // Create the delegate to process each entity returned in the pages. The delegate will cancel 
            // paging when the target subject is encountered.
            Func<TestEventItem, bool> processEachEvent = (e) =>
            {
                if (e.Subject.Contains("Subject3"))
                {
                    cancellationTokenSource.Cancel();
                }

                if (e.Subject.Contains("Subject for next page events"))
                {
                    Assert.Fail("Unexpectedly paged the next page of results.");
                }

                return true;
            };

            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent);
            await eventPageIterator.IterateAsync(pagingToken);

            // Assert the task was cancelled and did not get to the second page
            Assert.True(cancellationTokenSource.IsCancellationRequested, "The delegate page iterator did not cancel requests to fetch more pages.");
        }

        [Fact]
        public async Task Given_CollectionPage_Without_Next_Link_Property_It_Iterates_Across_PagesAsync()
        {
            // // Arrange the sample first page of 17 events to initialize the original collection page.
            var originalPage = new TestEventsDeltaResponse() { Value = new List<TestEventItem>() };
            originalPage.AdditionalData.Add("@odata.nextLink", JsonDocument.Parse("\"http://localhost/events?$skip=11\"").RootElement);
            var inputEventCount = 17;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            // Create the 5 events to initialize the next collection page.
            var nextPage = new TestEventsDeltaResponse() { Value = new List<TestEventItem>() };
            var nextPageEventCount = 5;
            for (int i = 0; i < nextPageEventCount; i++)
            {
                nextPage.Value.Add(new TestEventItem() { Subject = $"Subject for next page events: {i}" });
            }

            bool reachedNextPage = false;

            // Create the delegate to process each entity returned in the pages. The delegate will 
            // signal that we reached an event in the next page.
            Func<TestEventItem, bool> processEachEvent = (e) =>
            {
                if (e.Subject.Contains("Subject for next page events"))
                {
                    reachedNextPage = true;
                    return false;
                }

                return true;
            };

            this.mockRequestAdapter.Setup(x => x.SendAsync<TestEventsDeltaResponse>(It.IsAny<RequestInformation>(), It.IsAny<ParsableFactory<TestEventsDeltaResponse>>(), It.IsAny<Dictionary<string, ParsableFactory<IParsable>>>(), It.IsAny<CancellationToken>()))
                                    .Returns(() => { return Task.FromResult(nextPage); });

            // Act by calling the iterator
            var eventsDeltaPageIterator = PageIterator<TestEventItem, TestEventsDeltaResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent);
            await eventsDeltaPageIterator.IterateAsync();

            // Assert that paging was paused and got to the next page
            Assert.True(reachedNextPage, "The delegate page iterator did not reach the next page.");
            Assert.Equal(PagingState.Paused, eventsDeltaPageIterator.State);
        }

        [Fact]
        public async Task Given_CollectionPage_Delta_Link_Property_It_Iterates_Across_PagesAsync()
        {
            // // Arrange the sample first page of 17 events to initialize the original collection page.
            var originalPage = new TestEventsDeltaResponse() { Value = new List<TestEventItem>() };
            originalPage.OdataDeltaLink = "http://localhost/events?$skip=11";
            var inputEventCount = 17;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            Func<TestEventItem, bool> processEachEvent = (e) => true;

            // Act by calling the iterator
            var eventsDeltaPageIterator = PageIterator<TestEventItem, TestEventsDeltaResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent);
            await eventsDeltaPageIterator.IterateAsync();

            // Assert that paging was paused and got to the next page
            Assert.Equal(PagingState.Delta, eventsDeltaPageIterator.State);
            Assert.Equal("http://localhost/events?$skip=11", eventsDeltaPageIterator.Deltalink);
        }

        [Fact]
        public async Task Given_CollectionPage_Delta_Link_Property_It_Iterates_Across_Pages_And_ResumesAsync()
        {
            // // Arrange the sample first page of 17 events to initialize the original collection page.
            var eventBag = new List<TestEventItem>();
            var originalPage = new TestEventsDeltaResponse() { Value = new List<TestEventItem>() };
            originalPage.OdataDeltaLink = "http://localhost/events?$skip=11";
            var inputEventCount = 17;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            Func<TestEventItem, bool> processEachEvent = (e) =>
            {
                eventBag.Add(e);
                return true;
            };

            // Act by calling the iterator
            var eventsDeltaPageIterator = PageIterator<TestEventItem, TestEventsDeltaResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent);
            await eventsDeltaPageIterator.IterateAsync();

            // Assert that paging was paused and got to the next page
            Assert.Equal(PagingState.Delta, eventsDeltaPageIterator.State);
            Assert.Equal("http://localhost/events?$skip=11", eventsDeltaPageIterator.Deltalink);
            Assert.Equal(17, eventBag.Count);

            // create new page after the delta
            var nextPage = new TestEventsDeltaResponse() { Value = new List<TestEventItem>() };
            nextPage.OdataNextLink = "http://localhost/events?$skip=18";
            var nextPageEventCount = 10;
            for (int i = 0; i < nextPageEventCount; i++)
            {
                nextPage.Value.Add(new TestEventItem() { Subject = $"Subject for next page events: {i}" });
            }

            bool isFirstCall = true;
            this.mockRequestAdapter.Setup(x => x.SendAsync<TestEventsDeltaResponse>(It.IsAny<RequestInformation>(), It.IsAny<ParsableFactory<TestEventsDeltaResponse>>(), It.IsAny<Dictionary<string, ParsableFactory<IParsable>>>(), It.IsAny<CancellationToken>()))
                .Returns(() =>
                {
                    if (isFirstCall)
                    {
                        isFirstCall = false;
                    }
                    else
                    {
                        // let the second page have a delta link instead
                        nextPage.OdataNextLink = null;
                        nextPage.OdataDeltaLink = "http://localhost/events?$skip=145";
                    }

                    return Task.FromResult(nextPage);
                });


            // Resume the iteration
            await eventsDeltaPageIterator.IterateAsync();

            Assert.Equal(PagingState.Delta, eventsDeltaPageIterator.State);
            Assert.Equal("http://localhost/events?$skip=145", eventsDeltaPageIterator.Deltalink);
            Assert.Equal(37, eventBag.Count);// 17 initial items + 10 items from second page + 10 from last page
        }

        [Fact]
        public async Task Given_CollectionPage_It_Iterates_Across_Pages_With_Async_DelegateAsync()
        {
            // // Arrange the sample first page of 17 events to initialize the original collection page.
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>(), OdataNextLink = "http://localhost/events?$skip=11" };
            var inputEventCount = 17;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            // Create the 5 events to initialize the next collection page.
            var nextPage = new TestEventsResponse() { Value = new List<TestEventItem>() };
            var nextPageEventCount = 5;
            for (int i = 0; i < nextPageEventCount; i++)
            {
                nextPage.Value.Add(new TestEventItem() { Subject = $"Subject for next page events: {i}" });
            }

            bool reachedNextPage = false;

            // Create the async delegate to process each entity returned in the pages. The delegate will 
            // signal that we reached an event in the next page.
            Func<TestEventItem, Task<bool>> processEachEvent = async (e) =>
            {
                if (e.Subject.Contains("Subject for next page events"))
                {
                    await Task.Delay(100);// pause for no reason
                    reachedNextPage = true;
                    return false;
                }

                return true;
            };

            this.mockRequestAdapter.Setup(x => x.SendAsync<TestEventsResponse>(It.IsAny<RequestInformation>(), It.IsAny<ParsableFactory<TestEventsResponse>>(), It.IsAny<Dictionary<string, ParsableFactory<IParsable>>>(), It.IsAny<CancellationToken>()))
                                    .Returns(() => { return Task.FromResult(nextPage); });

            // Act by calling the iterator
            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent);
            Assert.True(eventPageIterator.IsProcessPageItemCallbackAsync);
            await eventPageIterator.IterateAsync();

            // Assert that paging was paused and got to the next page
            Assert.True(reachedNextPage, "The delegate page iterator did not reach the next page.");
            Assert.Equal(PagingState.Paused, eventPageIterator.State);
        }

        [Fact]
        public async Task Given_CollectionPage_It_Iterates_Across_PagesAsync()
        {
            // // Arrange the sample first page of 17 events to initialize the original collection page.
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>(), OdataNextLink = "http://localhost/events?$skip=11" };
            var inputEventCount = 17;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            // Create the 5 events to initialize the next collection page.
            var nextPage = new TestEventsResponse() { Value = new List<TestEventItem>() };
            var nextPageEventCount = 5;
            for (int i = 0; i < nextPageEventCount; i++)
            {
                nextPage.Value.Add(new TestEventItem() { Subject = $"Subject for next page events: {i}" });
            }

            bool reachedNextPage = false;

            // Create the delegate to process each entity returned in the pages. The delegate will 
            // signal that we reached an event in the next page.
            Func<TestEventItem, bool> processEachEvent = (e) =>
            {
                if (e.Subject.Contains("Subject for next page events"))
                {
                    reachedNextPage = true;
                    return false;
                }

                return true;
            };

            this.mockRequestAdapter.Setup(x => x.SendAsync<TestEventsResponse>(It.IsAny<RequestInformation>(), It.IsAny<ParsableFactory<TestEventsResponse>>(), It.IsAny<Dictionary<string, ParsableFactory<IParsable>>>(), It.IsAny<CancellationToken>()))
                                    .Returns(() => { return Task.FromResult(nextPage); });

            // Act by calling the iterator
            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent);
            await eventPageIterator.IterateAsync();

            // Assert that paging was paused and got to the next page
            Assert.False(eventPageIterator.IsProcessPageItemCallbackAsync);
            Assert.True(reachedNextPage, "The delegate page iterator did not reach the next page.");
            Assert.Equal(PagingState.Paused, eventPageIterator.State);
        }

        [Fact]
        public async Task Given_ApiError_It_Shows_Helpful_MessageAsync()
        {
            // // Arrange the sample first page of 17 events to initialize the original collection page.
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>(), OdataNextLink = "http://localhost/events?$skip=11" };
            var inputEventCount = 17;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            // Create the delegate to process each entity returned in the pages. The delegate will 
            // signal that we reached an event in the next page.
            Func<TestEventItem, bool> processEachEvent = (e) =>
            {
                if (e.Subject.Contains("Subject for next page events"))
                {
                    return false;
                }
                return true;
            };

            var errorResponseMessage = new HttpResponseMessage()
            {
                StatusCode = HttpStatusCode.BadRequest,
                Content = new StringContent(@"{
                    ""error"": {
                        ""code"": ""ErrorInvalidParameter"",
                        ""message"": ""The parameter is not currently supported on the resource."",
                        ""innerError"": {
                            ""request-id"": ""e8a0a3c8-7e8d-4b0b-8a0a-3c87e8d4b0b8"",
                            ""date"": ""2019-08-01T19:26:29""
                        }
                    }
                }", Encoding.UTF8, CoreConstants.MimeTypeNames.Application.Json)
            };

            using var testHttpMessageHandler = new TestHttpMessageHandler();
            testHttpMessageHandler.AddResponseMapping("http://localhost/events?$skip=11", errorResponseMessage);
            var customBaseClient = new BaseClient(new BaseRequestAdaptor(new AnonymousAuthenticationProvider(), httpClient: ClientFactory.Create(finalHandler: testHttpMessageHandler)));
            ApiClientBuilder.RegisterDefaultDeserializer<JsonParseNodeFactory>();

            // Act by calling the iterator
            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(customBaseClient, originalPage, processEachEvent);
            var serviceException = await Assert.ThrowsAsync<ServiceException>(() => eventPageIterator.IterateAsync());

            Assert.Equal(ErrorConstants.Messages.PageIteratorRequestError, serviceException.Message);
            Assert.NotNull(serviceException.InnerException);
            Assert.Equal("ErrorInvalidParameter : The parameter is not currently supported on the resource.", serviceException.InnerException.Message);
            Assert.Equal(400, serviceException.ResponseStatusCode);// matching status code
        }

        [Fact]
        public async Task Given_CollectionPage_It_Detects_Next_Link_LoopAsync()
        {
            // Create the 17 events to initialize the original collection page.
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>(), OdataNextLink = "http://localhost/events?$skip=11" };
            var inputEventCount = 5;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            // Create the 5 events to initialize the next collection page.
            var nextPage = new TestEventsResponse() { Value = new List<TestEventItem>(), OdataNextLink = "http://localhost/events?$skip=11" };//same next link url
            var nextPageEventCount = 5;
            for (int i = 0; i < nextPageEventCount; i++)
            {
                nextPage.Value.Add(new TestEventItem() { Subject = $"Subject for next page events: {i}" });
            }

            // Create the delegate to process each entity returned in the pages. The delegate will 
            // signal that we reached an event in the next page.
            Func<TestEventItem, bool> processEachEvent = (e) =>
            {
                return true;
            };

            this.mockRequestAdapter.Setup(x => x.SendAsync<TestEventsResponse>(It.IsAny<RequestInformation>(), It.IsAny<ParsableFactory<TestEventsResponse>>(), It.IsAny<Dictionary<string, ParsableFactory<IParsable>>>(), It.IsAny<CancellationToken>()))
                                    .Returns(() => { return Task.FromResult(nextPage); });

            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent);

            // Assert that the exception is thrown since the next page had the same nextLink URL
            ServiceException exception = await Assert.ThrowsAsync<ServiceException>(() => eventPageIterator.IterateAsync());
            Assert.Contains("Detected nextLink loop", exception.Message);
        }

        [Fact]
        public async Task Given_CollectionPage_It_Handles_Empty_NextPageAsync()
        {
            try
            {
                // Create the 17 events to initialize the original collection page.
                var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>(), OdataNextLink = "http://localhost/events?$skip=11" };
                var inputEventCount = 17;
                for (int i = 0; i < inputEventCount; i++)
                {
                    originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
                }

                // Create empty next collection page.
                var nextPage = new TestEventsResponse() { Value = new List<TestEventItem>() };

                // Create the delegate to process each entity returned in the pages. 
                Func<TestEventItem, bool> processEachEvent = (e) =>
                {
                    return true;
                };

                this.mockRequestAdapter.Setup(x => x.SendAsync<TestEventsResponse>(It.IsAny<RequestInformation>(), It.IsAny<ParsableFactory<TestEventsResponse>>(), It.IsAny<Dictionary<string, ParsableFactory<IParsable>>>(), It.IsAny<CancellationToken>()))
                                    .Returns(() => { return Task.FromResult(nextPage); });

                eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent);
                await eventPageIterator.IterateAsync();

                // Assert that we have made it through without any errors
                Assert.True(true);
            }
            catch (Exception)
            {
                Assert.Fail("Unexpected exception occurred when next page contains no elements.");
            }
        }

        [Fact]
        public void Given_PageIterator_It_Has_PagingState_NotStarted()
        {
            // Arrange
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>() };

            // Act
            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, (e) => { return true; });

            // Assert
            Assert.Equal(PagingState.NotStarted, eventPageIterator.State);
        }

        [Fact]
        public async Task Given_RequestConfigurator_It_Is_InvokedAsync()
        {
            // Create the 17 events to initialize the original collection page.
            var originalPage = new TestEventsResponse() { Value = new List<TestEventItem>(), OdataNextLink = "http://localhost/events?$skip=11" };
            var inputEventCount = 17;
            for (int i = 0; i < inputEventCount; i++)
            {
                originalPage.Value.Add(new TestEventItem() { Subject = $"Subject{i}" });
            }

            // Create the 5 events to initialize the next collection page.
            var nextPage = new TestEventsResponse() { Value = new List<TestEventItem>() };
            var nextPageEventCount = 5;
            for (int i = 0; i < nextPageEventCount; i++)
            {
                nextPage.Value.Add(new TestEventItem() { Subject = $"Subject for next page events: {i}" });
            }

            // Create the delegate to process each entity returned in the pages. 
            Func<TestEventItem, bool> processEachEvent = (e) => { return true; };

            // Create the delegate to configure the next page request. The delegate will signal that it was invoked.
            var requestConfiguratorInvoked = false;

            Func<RequestInformation, RequestInformation> requestConfigurator = (request) =>
            {
                requestConfiguratorInvoked = true;
                return request;
            };

            this.mockRequestAdapter.Setup(x => x.SendAsync<TestEventsResponse>(It.IsAny<RequestInformation>(), It.IsAny<ParsableFactory<TestEventsResponse>>(), It.IsAny<Dictionary<string, ParsableFactory<IParsable>>>(), It.IsAny<CancellationToken>()))
                    .Returns(() => { return Task.FromResult(nextPage); });

            eventPageIterator = PageIterator<TestEventItem, TestEventsResponse>.CreatePageIterator(baseClient, originalPage, processEachEvent, requestConfigurator);
            await eventPageIterator.IterateAsync();

            // Assert that configurator is invoked
            Assert.True(requestConfiguratorInvoked, "The delegate request configurator not invoked.");
        }
    }
}
