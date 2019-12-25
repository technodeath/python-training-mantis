import re

class SignupHelper:

    def __init__(self, app):
        self.app = app

    def decode_url(self, url):  #encoder for Mantis 2.23.0
        wd = self.app.wd
        wd.get('https://www.webatic.com/quoted-printable-convertor')
        wd.find_element_by_name("encoded").send_keys(url)
        wd.find_element_by_css_selector("input[value='Decode']").click()
        return wd.find_element_by_name("decoded").text

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.baseUrl + "/signup_page.php")
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_css_selector("input[type='submit']").click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)
        decoded_url = self.decode_url(url)

        wd.get(decoded_url)
        wd.find_element_by_css_selector("#realname").send_keys(username)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password_confirm").send_keys(password)
        wd.find_element_by_css_selector("button[type='submit']").click()

    def extract_confirmation_url(self, text):
        return re.search("http://((.*\n){4})", text, re.MULTILINE).group(0)  #for mantis 2.23.0 with 3 lines encoded url

