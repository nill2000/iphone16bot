from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
	browser = pw.firefox.launch(headless=False)
	page = browser.new_page()

	# page.goto("https://www.apple.com/")
	# print("On Apple Page")
	# page.wait_for_timeout(3000)

	# page.locator(".globalnav-link-iphone > span:nth-child(1) > span:nth-child(1)").click()
	# print("Clicked Iphone Header")
	# page.wait_for_timeout(3000)


	# page.locator("li.chapternav-item:nth-child(1) > a:nth-child(1)").click()
	# print("Clicked Iphone16")
	# page.wait_for_timeout(3000)

	# page.locator(".detail-ctas-link").click()
	# print("Clicked Buy")
	# page.wait_for_timeout(3000)

	page.goto("https://www.apple.com/shop/buy-iphone/iphone-16-pro")
	print("On Page")
	page.wait_for_timeout(3000)

	page.locator("#\:r6\:_label").click()
	print("Clicked Iphone option")
	page.wait_for_timeout(3000)

	page.click("li.colornav-item:nth-child(1) > label:nth-child(2)")
	print("Clicked Color")
	page.wait_for_timeout(3000)

	page.click("#\:rd\:_label")
	print("Clicked Storage")
	page.wait_for_timeout(3000)

	page.click("#noTradeIn_label")
	print("Clicked no trade in")
	page.wait_for_timeout(3000)

	page.click("div.rf-po-bfe-purchasegroupoption-container:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
	print("Clicked payment option")
	page.wait_for_timeout(3000)

	page.click("#\:rm\:_label")
	print("Clicked no carrier")
	page.wait_for_timeout(3000)

	page.click("#applecareplus_58_noapplecare_label")
	print("Clicked no coverage")
	browser.close()