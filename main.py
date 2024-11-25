from playwright.sync_api import sync_playwright

def main():
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

		page.click("#\:r6\:_label")
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
		page.wait_for_timeout(3000)
  
		page.click(".button")
		print("Clicked Added to bag")
		page.wait_for_timeout(3000)
  
		page.click(".rc-summaryheader-button > form:nth-child(1) > button:nth-child(1)")
		print("Clicked review bag")
		page.wait_for_timeout(3000)
  
		page.click("#shoppingCart\.actions\.navCheckoutOtherPayments")
		print("Clicked checkout")
		page.wait_for_timeout(3000)
  
		page.click("#signIn\.guestLogin\.guestLogin")
		print("Continue as guest")
		page.wait_for_timeout(3000)
  
		page.click(".rc-segmented-control-selected")
		print("Clicked delivery")
		page.wait_for_timeout(3000)
  
		page.click(".rs-edit-location-button")
		page.locator("#checkout\.fulfillment\.deliveryTab\.delivery\.deliveryLocation\.address\.postalCode").press_sequentially("77304")
		print("Editting zip code")
		page.wait_for_timeout(3000)
  
		page.click("#checkout\.fulfillment\.deliveryTab\.delivery\.deliveryLocation\.address\.calculate")
		print("Applied zip code")
		page.wait_for_timeout(3000)
  
		page.click(".form-selector-label")
		print("clicked delivery option 2")
		page.wait_for_timeout(3000)
  
		page.click("#rs-checkout-continue-button-bottom")
		print("Clicked continue to address")
		page.wait_for_timeout(3000)
  

		page.click("Closing Program")
		browser.close()
  
if __name__ == "__main__":
	main()
		


