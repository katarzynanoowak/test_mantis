from model.details import Details


class Project:

    def __init__(self, app):
        self.app = app

    def open_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("input[class='button-small']").click()

    def create(self, details):
        wd = self.app.wd
        self.open_add_new()
        self.fill_contact_form(details)
        self.submit()
        self.go_to_projects_page()

    def go_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_contact_form(self, details):
        wd = self.app.wd
        wd.find_element_by_id("project-name").send_keys(details.projectname)
        wd.find_element_by_id("project-description").send_keys(details.description)

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
            self.project_cache = []
            for row in wd.find_elements_by_tag_name("tr"):
                cell = row.find_elements_by_xpath("//*[@id='content']/div[2]/table/tbody/tr/td")
                text_projectname = cell[0].text
                text_description = cell[4].text
                self.project_cache.append(Details(projectname=text_projectname, description=text_description))
        return list(self.project_cache)

    def delete_first_project(self):
        wd = self.app.wd
        self.go_to_projects_page()
        wd.find_element_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[1]/td[1]/a").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[class='button']").click()




