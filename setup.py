
from setuptools import setup, find_packages

package_data = ['templates/bscontrolpanel/*.html', 'static/bscontrolpanel/css/*.css',
                'static/bscontrolpanel/js/*.js', 'static/bscontrolpanel/img/*']
dependencies = []

setup(name = "bscontrolpanel",
      version = "0.0.1",
      description = "A controlpanel app for bscms",
      author = "Justin Michalicek",
      author_email = "jmichalicek@gmail.com",
      license = "www.opensource.org/licenses/bsd-license.php",
      packages = find_packages(),
      #'package' package must contain files (see list above)
      package_data = {'bscontrolpanel' : package_data },
      install_requires = dependencies,
      #test_suite = 'test_project',
      long_description = "A controlpanel app for bscms"
)
