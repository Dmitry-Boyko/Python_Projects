#interaction_with_element_inside_the_table

rows_list = driver.find_lements(by.XPATH, rows_xpath)
for row in rows_lts:
    cell_apps_list = row.find_elements(By.XPATH, cell_apps_xpath)
    for cell_app in cell_apps_list:
        cell_app.click()
