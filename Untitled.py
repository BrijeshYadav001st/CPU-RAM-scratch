#!/usr/bin/env python
# coding: utf-8

# # __Author__ = "Brijesh Yadav"
# __email__ = "bkumaryadav096@gmail.com" 
#   __Date__ = "26 - Oct - 2021"

# In[ ]:


import psutil , datetime, time , openpyxl


# # Enter Process ID: 5044

# In[ ]:


pid = int (input("Enter process ID:"))


# In[ ]:


def warning():
    cpuusage = psutil.cpu_percent(interval=1)

    if cpuusage>50:
        print("Cpu usage is above 50%",cpuusage)

    memoryview = psutil.virtual_memory().percent

    if memusage >50:

        print("Memory utilization is above 50%", memusage)



# In[ ]:


def monitor() :

    time = datetime.datetime.now().strftime("%y%m%d - %H:%M:%S")

    p = psutil.process(pid)
    cpu = p.cpu_percent (interval =1)/ psutil.cpu_count()

    memory_mb = p.memory_full_info().rss/(1024*1024)

    memory = p.memory_percent()

    path = r".\Monitor_Result.xlsx"

    file = openpyxl.load_workbook(path)
    sheet = file.active

    sheet.cell(column=1, row=sheet.max_row + 1 , value=time)
    sheet.cell(column=2, row=sheet.max_row , value=pid)
    sheet.cell(column=3, row=sheet.max_row, value=cpu)
    sheet.cell(column=4, row=sheet.max_row , value=memory_mb)
    sheet.cell(column=5, row=sheet.max_row , value=memory)

    file.save(path)


# In[ ]:


import schedule


# In[ ]:


schedule.every(1).second.do(warning)
schedule.every(5).second.do (monitor)

while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:




