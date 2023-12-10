#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1


# In[2]:


pip install requests beautifulsoup4 pandas



# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_shine_jobs(job_title, location, num_jobs=10):
    # Step 1: Get the webpage
    base_url = "https://www.shine.com/"
    search_url = f"{base_url}job-search/{job_title.replace(' ', '-').lower()}-jobs-in-{location.lower()}"
    response = requests.get(search_url)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    
    soup = BeautifulSoup(response.text, 'html.parser')


    job_listings = soup.find_all('div', class_='search_listing')
    scraped_data = []

    for job_listing in job_listings[:num_jobs]:
        job_title = job_listing.find('div', class_='job_title').text.strip()
        job_location = job_listing.find('span', class_='loc').text.strip()
        company_name = job_listing.find('div', class_='comp_name').text.strip()
        experience_required = job_listing.find('span', class_='exp').text.strip()

        job_data = {
            'Job Title': job_title,
            'Job Location': job_location,
            'Company Name': company_name,
            'Experience Required': experience_required
        }

        scraped_data.append(job_data)
    df = pd.DataFrame(scraped_data)

    return df
job_title = "Data Analyst"
location = "Bangalore"
num_jobs_to_scrape = 10

jobs_dataframe = scrape_shine_jobs(job_title, location, num_jobs_to_scrape)

print(jobs_dataframe)


# In[4]:


#2


# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_shine_jobs(job_title, location, num_jobs=10):
    # Step 1: Get the webpage
    base_url = "https://www.shine.com/"
    search_url = f"{base_url}job-search/{job_title.replace(' ', '-').lower()}-jobs-in-{location.lower()}"
    response = requests.get(search_url)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = soup.find_all('div', class_='search_listing')
    scraped_data = []

    for job_listing in job_listings[:num_jobs]:
        job_title = job_listing.find('div', class_='job_title').text.strip()
        job_location = job_listing.find('span', class_='loc').text.strip()
        company_name = job_listing.find('div', class_='comp_name').text.strip()

        job_data = {
            'Job Title': job_title,
            'Job Location': job_location,
            'Company Name': company_name
        }

        scraped_data.append(job_data)

    df = pd.DataFrame(scraped_data)

    return df

job_title = "Data Scientist"
location = "Bangalore"
num_jobs_to_scrape = 10

jobs_dataframe = scrape_shine_jobs(job_title, location, num_jobs_to_scrape)

print(jobs_dataframe)


# In[6]:


#3



# In[9]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_shine_jobs(job_title, location_filter, salary_filter, num_jobs=10):
    # Step 1: Get the webpage
    base_url = "https://www.shine.com/"
    search_url = f"{base_url}job-search/{job_title.replace(' ', '-').lower()}-jobs"
    response = requests.get(search_url)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None()

    soup = BeautifulSoup(response.text, 'html.parser')


    location_checkbox = soup.find('input', {'value': location_filter})
    if location_checkbox:
        location_checkbox['checked'] = True

    salary_checkbox = soup.find('input', {'value': salary_filter})
    if salary_checkbox:
        salary_checkbox['checked'] = True

    # Step 5: Scrape data for the first 10 jobs after applying filters
    job_listings = soup.find_all('div', class_='search_listing')
    scraped_data = []

    for job_listing in job_listings[:num_jobs]:
        job_title = job_listing.find('div', class_='job_title').text.strip()
        job_location = job_listing.find('span', class_='loc').text.strip()
        company_name = job_listing.find('div', class_='comp_name').text.strip()
        experience_required = job_listing.find('span', class_='exp').text.strip()

        job_data = {
            'Job Title': job_title,
            'Job Location': job_location,
            'Company Name': company_name,
            'Experience Required': experience_required
        }

        scraped_data.append(job_data)

    df = pd.DataFrame(scraped_data)

    return df
job_title = "Data Scientist"
location_filter = "Delhi/NCR"
salary_filter = "3-6 Lakhs"
num_jobs_to_scrape = 10

jobs_dataframe = scrape_shine_jobs(job_title, location_filter, salary_filter, num_jobs_to_scrape)


print(jobs_dataframe)


# #4

# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_sunglasses(num_listings=100):
    base_url = "https://www.flipkart.com/"
    search_query = "sunglasses
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    
    search_url = f"{base_url}search?q={search_query}"
    response = requests.get(search_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the search results. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    sunglasses_listings = soup.find_all('div', {'class': '_1AtVbE'})

    scraped_data = []
    for listing in sunglasses_listings[:num_listings]:
        brand = listing.find('div', {'class': '_2WkVRV'}).text.strip()
        description = listing.find('a', {'class': 'IRpwTa'}).text.strip()
        price = listing.find('div', {'class': '_30jeq3'}).text.strip()

        sunglasses_data = {
            'Brand': brand,
            'Product Description': description,
            'Price': price
        }

        scraped_data.append(sunglasses_data)

    df = pd.DataFrame(scraped_data)

    return df

sunglasses_dataframe = scrape_flipkart_sunglasses()

print(sunglasses_dataframe)


# In[10]:


#5


# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_reviews(url, num_reviews=100):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    reviews = soup.find_all('div', {'class': '_27M-vq'})

    scraped_data = []
    for review in reviews[:num_reviews]:
        rating = review.find('div', {'class': '_3LWZlK'}).text.strip()
        summary = review.find('p', {'class': '_2-N8zT'}).text.strip()
        full_review = review.find('div', {'class': 't-ZTKy'}).text.strip()

        review_data = {
            'Rating': rating,
            'Review Summary': summary,
            'Full Review': full_review
        }

        scraped_data.append(review_data)

    df = pd.DataFrame(scraped_data)
    return df

flipkart_url = "https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART"

iphone_reviews_dataframe = scrape_flipkart_reviews(flipkart_url, num_reviews=100
print(iphone_reviews_dataframe)


# In[12]:


#6


# In[13]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_sneakers(num_sneakers=100):
    base_url = "https://www.flipkart.com/"
    search_query = "sneakers"

    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    search_url = f"{base_url}search?q={search_query}"
    response = requests.get(search_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the search results. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')


    sneakers_listings = soup.find_all('div', {'class': '_1AtVbE'})
    
    scraped_data = []
    for listing in sneakers_listings[:num_sneakers]:
        brand = listing.find('div', {'class': '_2WkVRV'}).text.strip()
        description = listing.find('a', {'class': 'IRpwTa'}).text.strip()
        price = listing.find('div', {'class': '_30jeq3'}).text.strip()

        sneakers_data = {
            'Brand': brand,
            'Product Description': description,
            'Price': price
        }

        scraped_data.append(sneakers_data)
    df = pd.DataFrame(scraped_data)

    return df

sneakers_dataframe = scrape_flipkart_sneakers()

print(sneakers_dataframe)


# In[14]:


#8


# In[15]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_azquotes_top_quotes(num_quotes=1000):
    base_url = "https://www.azquotes.com/"

    
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    
    soup = BeautifulSoup(response.text, 'html.parser')
    top_quotes_url = base_url + soup.find('a', {'href': '/top-quotes'}).get('href')
    response = requests.get(top_quotes_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the Top Quotes page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes_list = soup.find_all('div', {'class': 'wrap-block'})
    scraped_data = []

    for quote in quotes_list[:num_quotes]:
        quote_text = quote.find('a', {'class': 'title'}).text.strip()
        author = quote.find('span', {'class': 'author'}).text.strip()
        quote_type = quote.find('div', {'class': 'kw-box'}).text.strip()

        quote_data = {
            'Quote': quote_text,
            'Author': author,
            'Type Of Quote': quote_type
        }

        scraped_data.append(quote_data)

    # Step 6: Create a DataFrame
    df = pd.DataFrame(scraped_data)

    return df
top_quotes_dataframe = scrape_azquotes_top_quotes(num_quotes=1000)

print(top_quotes_dataframe)


# In[16]:


#9


# In[17]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_prime_ministers_data():
    base_url = "https://www.jagranjosh.com/"


    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


    soup = BeautifulSoup(response.text, 'html.parser')

    gk_url = base_url + soup.find('a', {'href': '/general-knowledge'}).get('href')
    response = requests.get(gk_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the GK page. Status code: {response.status_code}")
        return None
    prime_ministers_url = gk_url + soup.find('a', {'href': '/list-of-all-prime-ministers-of-india-1568288285-1'}).get('href')
    response = requests.get(prime_ministers_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the Prime Ministers page. Status code: {response.status_code}")
        return None


    soup = BeautifulSoup(response.text, 'html.parser')

    prime_ministers_list = soup.find_all('tr', {'class': 'row2'})
    scraped_data = []

    for prime_minister in prime_ministers_list:
        columns = prime_minister.find_all('td')

        name = columns[0].text.strip()
        born_dead = columns[1].text.strip()
        term_of_office = columns[2].text.strip()
        remarks = columns[3].text.strip()

        prime_minister_data = {
            'Name': name,
            'Born-Dead': born_dead,
            'Term of Office': term_of_office,
            'Remarks': remarks
        }

        scraped_data.append(prime_minister_data)


    df = pd.


# In[18]:


#10


# In[19]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_most_expensive_cars():
    base_url = "https://www.motor1.com/"

    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    search_url = f"{base_url}news/?q=50+most+expensive+cars"
    response = requests.get(search_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the search results. Status code: {response.status_code}")
        return None

    
    soup = BeautifulSoup(response.text, 'html.parser')


    link = soup.find('a', {'href': '/news/377754/top-50-most-expensive-cars/'})
    if not link:
        print("Link not found.")
        return None

    most_expensive_cars_url = base_url + link['href']
    response = requests.get(most_expensive_cars_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page with the most expensive cars. Status code: {response.status_code}")
        return None


    soup = BeautifulSoup(response.text, 'html.parser')


    cars_list = soup.find_all('div', {'class': 'slideshow-item'})
    scraped_data = []

    for car in cars_list[:50]:
        car_name = car.find('h3').text.strip()
        car_price = car.find('span', {'class': 'price'}).text.strip()

        car_data = {
            'Car Name': car_name,
            'Price': car_price
        }

        scraped_data.append(car_data)


    df = pd.DataFrame(scraped_data)

    return df


most_expensive_cars_dataframe = scrape_most_expensive_cars()

print(most_expensive_cars_dataframe)


# In[ ]:




