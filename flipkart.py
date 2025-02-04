from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import re

def data_clean(data):
    data = re.sub('&amp;','&',str(data))
    data = re.sub('&quot;',"'",str(data))
    data = re.sub('&nbsp;','',str(data))
    data = re.sub('&#39;;',"';",str(data))
    data = re.sub('&#39;',"';",str(data))
    data = re.sub('&#xD;&#xA;',' ',str(data))
    data = re.sub('#x27;',"'",str(data))
    data = re.sub(r'\s+',' ',str(data))
    data = re.sub('<[^>]&?>','',str(data))
    return data
       
def single_regex(pattern,target_string):
    data = re.findall(pattern,target_string)
    if data != []:
        data = data[0]
    else:
        data = ''
    return data
 
     
output_data = "Sl.No\tProduct Name\tAnnual Power Usage\tRoom Size\tWarranty\tMRP\tOffer Price\tPercentage of Offer\tProduct Link\n"

with open("OutPut.txt", 'w') as OP:
    OP.write(output_data)

    
driver = webdriver.Chrome()

main_url = driver.get("https://www.flipkart.com/")
time.sleep(5)

try:
    close_login = driver.find_element(By.XPATH,'/html/body/div[3]/div/span').click()
    time.sleep(5)

except:
    clear_search = driver.find_element(By.CLASS_NAME,"Pke_EE").clear()
    time.sleep(5)
    search_key_word = driver.find_element(By.CLASS_NAME,"Pke_EE").send_keys("AC")
    time.sleep(5)
    submit_key = driver.find_element(By.XPATH,'//*[@type="submit"]').click()
    time.sleep(5)
    search_by_value = driver.find_element(By.XPATH,'//*[@value="40000"]').click()
    time.sleep(5)
    click_capasity = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[6]/div/div').click()
    time.sleep(5)
    click_capasity_value = driver.find_element(By.XPATH,'//*[@title="1.5.Ton"]').click()
    time.sleep(5)
    click_energy_rating = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[7]/div').click()
    time.sleep(5)
    select_energy_rating = driver.find_element(By.XPATH,'//*[@title="3Star"]').click()
    time.sleep(5)
    click_connectivity = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[16]/div/div').click()
    time.sleep(5)
    select_connectivity = driver.find_element(By.XPATH,'//*[@title="Yes"]').click()
    time.sleep(5)
    
    current_url = driver.current_url
    # print(f"Current URL: {current_url}")
    
    content_response = requests.get(current_url)
    response_code = content_response.status_code
    print(response_code)

    content = content_response.text
    time.sleep(5)

    with open('Result_page.html', 'w', encoding='utf-8') as SP:
        SP.write(content)
     
    num = 0
    blocks = re.findall(r'noreferrer\"\s*h[\w\W]*?class\=\"k6cAZE\s*[^>]*?>',str(content))
    for block in blocks:
        num += 1
       
        product_name = single_regex(r'class\=\"KzDlHZ\">([^>]*?)<\/div>',str(block))
        annual_power_usage = single_regex(r'Annual\s*Power\s*Usage\:([^>]*?)<',str(block))
        room_size = single_regex(r'Room\s*Size\:([^>]*?)<',str(block))
        warranty = single_regex(r'<li class="J\+igdf">([^>]*?)<\/li><\/ul>',str(block))
        mrp = single_regex(r'\₹<\![\w\w]*?[^>]*>([^>]*?)<',str(block))
        offer_price = single_regex(r'class\=\"Nx9bqj\s*\_4b5DiR\">\₹([^>]*?)<',str(block))
        percentage_of_offer = single_regex(r'<span>([^>]*?)<\/span><\/div>',str(block))
        product_url = single_regex(r'href\=\"([^>]*?)"',str(block))
        updated_url = "https://www.flipkart.com"+product_url
        
        
        output_data = f"{num}\t{product_name}\t{annual_power_usage}\t{room_size}\t{warranty}\t{mrp}\t{offer_price}\t{percentage_of_offer}\t{updated_url}\n"

        with open("OutPut.txt", 'a') as OP:
            OP.write(output_data)
print("Completed")
    
    
    
    
    
    
    
    
    
    
    
  
    
    
   
    
   
    
    
    