from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# تابع برای اسکرول کردن و کلیک کردن در سایت
def browse_site(driver, duration):
    end_time = time.time() + duration
    actions = ActionChains(driver)
    
    while time.time() < end_time:
        # اسکرول به پایین
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        
        # پیدا کردن و کلیک روی یک عنصر تصادفی (در اینجا همه لینک‌ها را انتخاب می‌کند)
        links = driver.find_elements(By.TAG_NAME, "a")
        if links:
            random_link = links[0]  # اینجا می‌توانیم به جای 0، عددی تصادفی برای انتخاب لینک داشته باشیم.
            actions.move_to_element(random_link).click().perform()
            time.sleep(2)  # صبر برای بارگذاری صفحه جدید
        
        # بازگشت به صفحه قبلی
        driver.back()
        time.sleep(2)  # صبر برای بارگذاری صفحه قبلی

# ایجاد یک مرورگر جدید و ورود به سایت
def main(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # باز کردن مرورگر در حالت ناشناس (یوزر جدید)
    
    # ساخت درایور کروم
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # باز کردن سایت
        driver.get(url)
        
        # اسکرول کردن و کلیک کردن به مدت 10 دقیقه (600 ثانیه)
        browse_site(driver, duration=600)
        
    finally:
        driver.quit()  # بستن مرورگر

# اجرای برنامه
if __name__ == "__main__":
    url = input("https://www.digikala.com/ ")
