selenium_driver.execute_script('jQuery("#dialog_ok_button").click();')

jQuery(".cssmenu li a:contains('Adjust Time Remaining')").click();

unction deleteTest() {
  jQuery("a[id*=deleteEventOrAccess]").click();
  return false;
}
deleteTest();
