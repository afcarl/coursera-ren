import os
''' U. washington Coursera courses use exceedingly long file names,
so we cannot download them in Windows. coursera-dl shortens the names
but not in an intelligent way (it just truncates, leaving bad names)

The following two functions are to be used in linux. They mostly rename
the directories and files to reasonable names. I still had to hand edit
some really long names! So, the idea is, run coursera-dl in linux to get
the course without truncating the name, load this module in ipython, run
rename_dir in the root dir of the course, and then run re2 to rename the
individual files. 
'''

def rename_dir():
  ''' strips out the - W01_L02_P01 - namewewant (01-34) type strings in some     
  coursera course directories''' 
  for f in os.listdir('.'):
    s = f.rsplit('(')[0][:-1]
    newf = s.split('-',1)[0] + '-' + s.rsplit('-',1)[1]
    # print newf
    os.rename (f, newf)

def re2():
  ''' strips out the - W01_L02_P01 - namewewant (01-34) type strings in some coursera course
  directories''' 
  for root, dirs, files in os.walk('.'):
    for f in files:
      try:
        if f.find('mp4') > -1 or f.find('srt') > -1 or f.find('.txt') > -1:
          s = f.rsplit('(')[0][:-1]
          ext = f.rsplit('.', 1)[1]
          newf = s.split('-',1)[0] + '-' + s.rsplit('-',1)[1] + '.' + ext
          #print os.path.join (root, f)
          #print os.path.join (root, newf)
          os.rename (os.path.join (root, f), os.path.join (root, newf))
      except:
       print 'passing on ', f
