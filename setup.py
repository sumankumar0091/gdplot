from distutils.core import setup
setup(
  name = 'greendeck_plot',         
  packages = ['greendeck_plot'],  
  version = '0.1',    
  license='MIT',       
  description = 'Plot Chart from your googlesheet',  
  author = 'Suman Kumar',                  
  author_email = 'sumankumar0091@gmail.com',      
  url = 'https://github.com/user/reponame', 
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',   
  keywords = ['Chart', 'gsheet', 'plot'],  
  install_requires=[         
          'pandas',
          'matplotlib.pyplot',
          'gsheets',
          'time',
          'os',
          'fnmatch', 
          'shutil'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
