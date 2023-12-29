from selenium import webdriver
import csv

# 定义搜索关键词
query = '大模型'

# 声明浏览器驱动
driver = webdriver.Chrome('chromedriver-win64/chromedriver.exe') # 需要替换为实际的驱动路径

# 打开谷歌搜索页面，并输入关键词
driver.get('https://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys(query)

# 模拟点击搜索按钮
search_button = driver.find_element_by_name('btnK')
search_button.click()

# 等待搜索结果加载完成
driver.implicitly_wait(10)

# 找到所有搜索结果的 HTML 元素
search_results = driver.find_elements_by_css_selector('搜索结果元素选择器')

# 创建 CSV 文件，并写入搜索结果
with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for result in search_results:
        # 获取搜索结果页面的标题和描述信息
        title = result.find_element_by_css_selector('标题元素选择器')
        snippet = result.find_element_by_css_selector('描述信息元素选择器')

        # 将标题和描述信息写入 CSV 文件中
        writer.writerow([title.text, snippet.text])

# 关闭浏览器
driver.quit()