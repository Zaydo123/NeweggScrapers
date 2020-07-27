from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

for i in range(1,29):

    my_url = 'https://www.newegg.com/p/pl?N=100007709&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_2&page='+str(i)
    #open and grab page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    #html parser
    page_soup = soup(page_html, "html.parser")

    #grabs each item
    containers = page_soup.findAll("div",{"class":"item-container"})
    print(len(containers), "items")

    contain = containers[0]
    container = containers[0]

    out_filename = "gpuScrape.csv"
    f = open(out_filename, "a+")

    headers = "brand, product_name, shipping, truncatedPrice, link \n"
    f.write(headers)

    for container in containers:
        brand = container.div.div.a.img['title']
        title_container = container.findAll("a",{"class":"item-title"})
        product_name = title_container[0].text
        shipping_container = container.findAll("li", {"class":"price-ship"})
        shipping = shipping_container[0].text.strip()


        unprice=container.find_all("div",{"class":"item-action"})
        price = unprice[0].text.strip()
        truncatedPrice = price[0:7]
        print(truncatedPrice)


        link = container.findAll("a",{"class":"item-rating"})
        link[26:100]
        print(link)

        f.write(str(brand) + "," + product_name.replace(",", "|") + "," + shipping + ","+truncatedPrice + "," + str(link) +"\n")


    f.close()
