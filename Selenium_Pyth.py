# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:08:21 2017

@author: '...'
"""

"""
Correr los primeros para actualizar el PIP de Python e instalar virtual environments & selenium
# python -m pip install -U pip setuptools
# pip install virtualenv
# pip install selenium
"""



import re, csv
from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

"""
Comentarios acerca de la paquetería usada:

Paquetería RANDOM: generación aleatoria de números.

Paquetería Selenium:

** webdriver **

Creación del driver a utilizar: Chrome, IE, Firefox o Remote. 

** By **

Define posibles criterios de búsqueda para objetos dentro de una página

- Name
- Class Name
- CSS Selector
- ID
- Link Text
- Xpath

** WebDriverWait **

Pausas dentro de una página, se utiliza como: WebDriverWait(driver, timeout, poll_frequency = .5 , ignored_exceptions = None)

- Timeout = # seconds before timing out
- poll_frequency = sleep interval between calls (default .5 seconds)

** ActionChains

Low level interactions: Mouse Movement, Mouse Button Actions, Key Press, Context Menu Interactions.

Functions:

- click(on_element=None) , Clicks an element.
Args : on_element: The element to click. If None, clicks on current mouse position.

- click_and_hold(on_element=None), Holds down the left mouse button on an element.
Args : on_element: The element to mouse down. If None, clicks on current mouse position.

- context_click(on_element=None), Performs a context-click (right click) on an element.
Args : on_element: The element to context-click. If None, clicks on current mouse position.

- double_click(on_element=None), Double-clicks an element.
Args : on_element: The element to double-click. If None, clicks on current mouse position.

- drag_and_drop(source, target), Holds down the left mouse button on the source element,
then moves to the target element and releases the mouse button.
Args : [source: The element to mouse down. , target: The element to mouse up.]

- drag_and_drop_by_offset(source, xoffset, yoffset), Holds down the left mouse button on the source element,
then moves to the target offset and releases the mouse button.
Args : [source: The element to mouse down., xoffset: X offset to move to., yoffset: Y offset to move to.]

- key_down(value, element=None), Sends a key press only, without releasing it.
Args : [value: The modifier key to send. Values are defined in Keys class., element: The element to send keys. If None, sends a key to current focused element.]
Example, pressing ctrl+c:
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
- key_up(value, element=None)
Releases a modifier key.

- move_by_offset(xoffset, yoffset)

- move_to_element(to_element), optional movements inside the element with xoffset and yoffset

- perform(), Performs all stored actions.

- release(on_element=None), Releasing a held mouse button on an element.

- reset_actions(), Clears actions that are already stored on the remote end.

- send_keys(*keys_to_send), Sends keys to current focused element.
- send_keys_to_element(element, *keys_to_send)

** expected_conditions

Busca determinar condiciones de elementos en una página

Funciones:

- class selenium.webdriver.support.expected_conditions.alert_is_present
Expect an alert to be present.
- class selenium.webdriver.support.expected_conditions.element_located_selection_state_to_be(locator, is_selected)
An expectation to locate an element and check if the selection state specified is in that state. locator is a tuple of (by, path) is_selected is a boolean

- class selenium.webdriver.support.expected_conditions.element_located_to_be_selected(locator)
An expectation for the element to be located is selected. locator is a tuple of (by, path)

- class selenium.webdriver.support.expected_conditions.element_selection_state_to_be(element, is_selected)
An expectation for checking if the given element is selected. element is WebElement object is_selected is a Boolean.”

- class selenium.webdriver.support.expected_conditions.element_to_be_clickable(locator)
An Expectation for checking an element is visible and enabled such that you can click it.

- class selenium.webdriver.support.expected_conditions.element_to_be_selected(element)
An expectation for checking the selection is selected. element is WebElement object

- class selenium.webdriver.support.expected_conditions.frame_to_be_available_and_switch_to_it(locator)
An expectation for checking whether the given frame is available to switch to. If the frame is available it switches the given driver to the specified frame.

- class selenium.webdriver.support.expected_conditions.invisibility_of_element_located(locator)
An Expectation for checking that an element is either invisible or not present on the DOM.

- class selenium.webdriver.support.expected_conditions.new_window_is_opened(current_handles)
An expectation that a new window will be opened and have the number of windows handles increase

- class selenium.webdriver.support.expected_conditions.number_of_windows_to_be(num_windows)
An expectation for the number of windows to be a certain value.

- class selenium.webdriver.support.expected_conditions.presence_of_all_elements_located(locator)
An expectation for checking that there is at least one element present on a web page. locator is used to find the element returns the list of WebElements once they are located

- class selenium.webdriver.support.expected_conditions.presence_of_element_located(locator)
An expectation for checking that an element is present on the DOM of a page. This does not necessarily mean that the element is visible. locator - used to find the element returns the WebElement once it is located

- class selenium.webdriver.support.expected_conditions.staleness_of(element)
Wait until an element is no longer attached to the DOM. element is the element to wait for. returns False if the element is still attached to the DOM, true otherwise.

- class selenium.webdriver.support.expected_conditions.text_to_be_present_in_element(locator, text_)
An expectation for checking if the given text is present in the specified element. locator, text

- class selenium.webdriver.support.expected_conditions.text_to_be_present_in_element_value(locator, text_)
An expectation for checking if the given text is present in the element’s locator, text

- class selenium.webdriver.support.expected_conditions.title_contains(title)
An expectation for checking that the title contains a case-sensitive substring. title is the fragment of title expected returns True when the title matches, False otherwise

- class selenium.webdriver.support.expected_conditions.title_is(title)
An expectation for checking the title of a page. title is the expected title, which must be an exact match returns True if the title matches, false otherwise.

- class selenium.webdriver.support.expected_conditions.visibility_of(element)
An expectation for checking that an element, known to be present on the DOM of a page, is visible. Visibility means that the element is not only displayed but also has a height and width that is greater than 0. element is the WebElement returns the (same) WebElement once it is visible

- class selenium.webdriver.support.expected_conditions.visibility_of_all_elements_located(locator)
An expectation for checking that all elements are present on the DOM of a page and visible. Visibility means that the elements are not only displayed but also has a height and width that is greater than 0. locator - used to find the elements returns the list of WebElements once they are located and visible

- class selenium.webdriver.support.expected_conditions.visibility_of_any_elements_located(locator)
An expectation for checking that there is at least one element visible on a web page. locator is used to find the element returns the list of WebElements once they are located

- class selenium.webdriver.support.expected_conditions.visibility_of_element_located(locator)
An expectation for checking that an element is present on the DOM of a page and visible. Visibility means that the element is not only displayed but also has a height and width that is greater than 0. locator - used to find the element returns the WebElement once it is located and visible

** NoSuchElementException

Cuando no se encuentra un elemento.

- exception selenium.common.exceptions.NoSuchElementException(msg=None, screen=None, stacktrace=None)

If you encounter this exception, you may want to check the following:
Check your selector used in your find_by...
Element may not yet be on the screen at the time of the find operation, (webpage is still loading)


"""

def write_stat(loops, time):
    with open('stat.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([loops, time])

"""
La función 'write_stat' crea un archivo delimitado por comas en donde se guardarán los resultados del proceso de quebrar el recaptcha para fines de análisis (loops, time).
"""

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

"""
La función 'check_exists_by_xpath' busca un elemento... es binaria mapeada a las funciones lógicas de Python.
"""

def wait_between(a,b):
    rand=uniform(a, b)
    sleep(rand)

"""
La función 'wait_between' define un tiempo aleatorio de espera, los límites de la distribución son los argumentos. 
"""

def dimention(driver):
    d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1]);
    return d if d else 3  # dimention is 3 by default

"""
La función 'dimention' actúa una vez que se abren las opciones de imágenes a seleccionar para 
"""

# ***** main procedure to identify and submit picture solution
def solve_images(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID ,"rc-imageselect-target"))
        )
    dim = dimention(driver)
    # ****************** check if there is a clicked tile ******************
    if check_exists_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]'):
        rand2 = 0
    else:
        rand2 = 1

    # wait before click on tiles
    wait_between(0.5, 1.0)
    # ****************** click on a tile ******************
    tile1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH ,   '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim ))))
        )
    tile1.click()
    if (rand2):
        try:
            driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim), randint(1, dim))).click()
        except NoSuchElementException:
            print('\n\r No Such Element Exception for finding 2nd tile')


    #****************** click on submit buttion ******************
    driver.find_element_by_id("recaptcha-verify-button").click()

start = time()
url='http://www.cre.gob.mx/ConsultaPrecios/GasLP/PlantaDistribucion.html?idiom=es'
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application")
driver.get(url)

mainWin = driver.current_window_handle

# move the driver to the first iFrame
driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])

# *************  locate CheckBox  **************
CheckBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))
        )

# *************  click CheckBox  ***************
wait_between(0.5, 0.7)
# making click on captcha CheckBox
CheckBox.click()

#***************** back to main window **************************************
driver.switch_to_window(mainWin)

wait_between(2.0, 2.5)

# ************ switch to the second iframe by tag name ******************
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[1])
i=1
while i<130:
    print('\n\r{0}-th loop'.format(i))
    # ******** check if checkbox is checked at the 1st frame ***********
    driver.switch_to_window(mainWin)
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME , 'iframe'))
        )
    wait_between(1.0, 2.0)
    if check_exists_by_xpath('//span[@aria-checked="true"]'):
                import winsound
        winsound.Beep(400,1500)
        write_stat(i, round(time()-start) - 1 ) # saving results into stat file
        break

    driver.switch_to_window(mainWin)
    # ********** To the second frame to solve pictures *************
    wait_between(0.3, 1.5)
    driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[1])
    solve_images(driver)
    i=i+1
