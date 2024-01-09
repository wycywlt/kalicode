import asyncio
from pyppeteer import launch
from lxml import etree

async def main():
    # Launch a headless browser
    browser = await launch(headless=False)


    # Create a new page
    page = await browser.newPage()
    print("Browser launched successfully!")

    try:
        # Navigate to a webpage
        await page.goto('http://quotes.toscrape.com/js/')

        # Capture page content
        page_content = await page.content()

        # Parse HTML content using lxml
        tree = etree.HTML(page_content)

        # Extract information from the page
        quotes = tree.xpath('//div[@class="quote"]/span[@class="text"]/text()')
        authors = tree.xpath('//div[@class="quote"]/span/small[@class="author"]/text()')

        # Print the quotes and authors
        for quote, author in zip(quotes, authors):
            print(f'"{quote}" - {author}')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        await browser.close()

# Create a coroutine object
coroutine = main()

# Create and run the event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
