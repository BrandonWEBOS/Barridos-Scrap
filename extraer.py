#https://business.walmart.com/cp/hospitality/2407105
#https://www.fahorro.com/cuidado-personal/me-quiero-bien/alimentos-saludables.html
#https://www.homedepot.com.mx/pinturas
#https://www.coppel.com/SearchDisplay?categoryFacetHierarchyPathName=Deportes&searchType=1002&advancedSearch=&pageSize=24&filterTerm=&searchTermScope=&storeId=10151&pageView=grid&manufacturer=&urlLangId=-5&sType=SimpleSearch&metaData=&catalogId=10051&searchTerm=RB2346EPMTPEJUGUETESRYMICONOGRAFIA&resultCatEntryType=2&showResultsPage=true&minPrice=&beginIndex=0&top_category=&maxPrice=&langId=-5&categoryFacetHierarchyPath=250501&categoryId=250501
#https://www.farmaciasdesimilares.com/#!/medicamentos

from bs4 import BeautifulSoup
import requests

website = 'https://www.farmaciasdesimilares.com/#!/medicamentos'
results = requests.get(website)
content = results.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())