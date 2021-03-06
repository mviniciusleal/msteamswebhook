from distutils.core import setup
setup(
  name = 'msteamswebhook',         # How you named your package folder (MyLib)
  packages = ['msteamswebhook'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Send adaptative cards with teams webhooks',   # Give a short description about your library
  author = 'Marcus Vinicius Leal',                   # Type in your name
  author_email = 'your.email@domain.com',      # Type in your E-Mail
  url = 'https://github.com/mviniciusleal/msteamswebhook',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mviniciusleal/msteamswebhook/archive/v_05.tar.gz',    # I explain this later on
  keywords = ['teams', 'msteams', 'adaptative', 'card', 'webhook'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)