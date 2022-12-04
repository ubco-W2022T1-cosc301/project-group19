# Introduction
The dataset our group has chosen is from the British Columbia Ministry of Education. It demonstrates the British Columbia Completion Rate for high school students between the years of 1997/98 to 2020/2021 with information on cohorts, students, success rates, outmigrant counts and more. We believe it is essential to understand our province's success rates and high school information as we entrust the British Columbia Ministry of Education to teach the following generations. With this in mind, it becomes relevant to understand whether the curriculum students follow is working successfully. We were also interested in population compared to completion rates as a trend of low completion rates in areas with smaller populations could hint at a more significant problem that those in British Columbia should be aware of. Lastly, as students ourselves, we were curious about how the completion rates have changed over time and if there was a more extensive importance on education or less of a priority since 1997. Overall our role as students has led us to feel particularly passionate about this data, especially since 2/3 of our group members are included in this dataset. 

![School](https://www.trailtimes.ca/wp-content/uploads/2020/08/22529919_web1_191128-CAN-SHSS-school-1024x683.jpg)

## Question 1:
My (Denis) main research question was to see if dogwood completion rates have increased over the years, with a newer mentality of "Post-Secondary School is extremely important & needed to succeed in life" that has been placed on the younger generation. In the past, high paying jobs or even livable careers did not require a Post-Secondary Degree, however this has shifted to degrees are nearly required for most jobs. My secondary question is to see if Indigenous graduation rates have increased,decreased or remained fairly level for the past ~20 years. As well as Students with Disabilities. The answer these questions we first must look at the overall estimated completion rates over the years. As this will be our main way of measuring the graduation rates and seeing change. 


![Figure 1](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/DGFig1.PNG)

In Figure 1, we can clearly see a consistent increase in Completion rates. I cannot say that this is because the importance of post-secondary school has increased, or other socialite norms have applied pressure onto students to finish school. All I can say is that definitively, Students tend to finish their dogwood diploma more often in current years versus past. This also does not say that post-Secondary enrollment have increased but more likely than not, people are finishing high school more often be it either that most jobs now require a minimum of a Highschool Diploma or less reason to drop out.

![Figure 2](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/DGFig2.PNG)

This graph shows that while Indigenous graduation rate is consistently lower than non-Indigenous, the rates are in fact increasing alongside the non-Indigenous rates! This is exciting to see! This also shows an interesting piece of information, General Non-Indigenous students graduation rates have not increased all that much over the years comparatively. Now let's take a look at Student with Disabilities!

![Figure 3](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/DGFig3.PNG)

Just like the Indigenous rates, Students with Disabilities follows a similar pattern of increase! This could be from better education or better support for those students, allowing them to succeed often. So overall, the data shows that graduation rates have in fact increased over the years! Not only general students but even the diverse types! There has been a constant increase in both Indigenous and Students with Disabilities graduation rates over the years. This in turn creates an increased overall graduation rate! While general students’ rates have barely increased when compared to the other two subsections of students, they have also increased. Meaning that every subsection of students has increased they overall graduation rates every year, therefore the total completion rate has increased heavily since 1997!

[If you would like to see a more indepth analysis, you can find the full notebook here](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/notebooks/analysis1.ipynb)

## Question 2:
#### Does your school district's population affect your likelihood to graduate from high school?

My research question is whether the population size of the district in which a school is located has a relationship with the proportion of students receiving their high school diploma. My secondary research question is if there is consistency in population size among those school districts that have lower than 70% average estimated completion rates. In order to conduct my analysis, I merged a second dataset comprising of population data for each of the school districts in BC. 

I categorized the school districts into four groups based on population size to compare their respective completion rates to see if there is a relationship present. 


### Figure 1.1 - Population Group 1: >100,000
#### Average Estimated Completion Rate = 85.5%
![Figure 1_1](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/APFig1_1.png)

Figure 1 plots school districts with population above 100,000 and their respective average estimated completion rates. The average estimated completion rate for population group 1 is 85.5%, the highest of all four population groups. Most of the school districts have exceptional completion rates, rangin from 78% to 92%. It is interesting to note that only one of the school districts in this group has a completion rate lower than 80% (Nanaimo-Ladysmith).

### Figure 1.2 - Population Group 2: 50,000 - 99,999
#### Average Estimated Completion Rate = 80.18%
![Figure 1_2](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/APFig1_2.png)

Figure 2 plots school districts with population between 50,000 and 99,999 and their respective average estimated completion rates. The average estimated completion rate for population group 2 is 80.18%. Most of the school districts in this population group have completion rates around the high 70s. At the bottom of this group, with a population size of 51,268, West Vancouver has the highest completion rate of all of the school districts in BC, 98%. Although my analysis does not dive into the reason for this outlier, I hypothesize that it could be related to the higher income/wealth in that school district. 

### Figure 1.3 - Population Group 3: 25,000 - 49,999
#### Average Estimated Completion Rate = 79.55%
![Figure 1_3](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/APFig1_3.png)

Figure 3 plots school districts with population between 50,000 and 99,999 and their respective average estimated completion rates. The average estimated completion rate for population group 3 is 79.55%, slightly lower than that of population group 2.


### Figure 1.4 - Population Group 4: < 25,000
#### Average Estimated Completion Rate = 72.35%
![Figure 1_4](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/APFig1_4.png)

Figure 4 plots school districts with population below 25,000 and their respective average estimated completion rates. The average estimated completion rate for population group 4 is 72.35%, the lowest of all four population groups. The completion rates in this population group range from 52%-87%. It is interesting to note that the two lowest completion rates of all school districts, 52% and 58% also have the smallest population sizes, Nisga'a and Stikine, respectively. 



To expand on my analysis, I am looking more in depth at the school districts with the lowest completion rates, those under 70%. I would like to see if there is any commonality between them in regards to population size. 

![Figure 2](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/APFig2.jpeg)

As seen in Figure 2, there are seven school districts with an estimated completion rate below 70%. It is interesting to note that all of these school districts have a population lower than 25,000 and the three lowest completion rates (52%, 58%, and 63%) also have the three lowest population sizes, all under 5,000 people (Nisga'a, Stikine, and Vancouver Island West).


By comparing all four of these figures, it is clear that there exists a positive relationship between population size of the school district and its completion rate. On average, the higher the population, the better chance to have higher completion rates and vice versa. 

[You can find the full analysis notebook here, including the code and the data here](notebooks/analysis2.ipynb) 

## Question 3:
[You can find the full analysis notebook here, including the code and the data here](notebooks/analysis3.ipynb) 
#### To discover if graduation rates have declined or risen over time and to consider what environmental factors could lead to these changes.


![Figure 1](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/Julia%20fig1%20Q1.jpg)

**Figure 1.** acts as an excellent visual when trying to understand completion rates over the years. The graph begins in 1997 and peaks in 2021 (the end of our dataset). While the graph does have slight variations over the years, it is clear that there was a higher graduation rate as time went on. I believe there is currently more pressure on students to graduate highschool and it is definetly considered the the societle norm to recieve your highschool education and diplThe graph above is an excellent visual for understanding completion rates over the years. The graph begins in 1997 and peaks in 2021 (the end of our dataset). While the graph does have slight variations over the years, it is clear that there was a higher graduation rate as time went on. There is currently more pressure on students to graduate high school, and it is considered the social norm to receive your high school education and diploma at a minimum. The steepest peak of my graph occurs between 1987 and 1989, where the estimated completion rate line is almost vertical on the graph. Figure 3. is an asset in understanding the graduation rates, as you must understand the correlation between the attendance rates and completion rates to realize that the majority of students are very successful. The similarity between the two graphs is promising.

Regarding my research question, graduation rates/completion rates have risen since 1997. I initially wondered if the introduction of modern-day technology would lead to an incline in graduation rates as there is a perception that technology is making us lazy but also that technology provides access to online education. Some students may drop out of public schools for a preferable online learning system. When analyzing the data, my hypothesis was incorrect, and there is not a large enough decline in completion rates to make this a considerable argument.oma at minimum. The steepest peak of my graph occurs between the years of 1987 and 1989 where the estimated completion rate line is almost vertical on the graph.

![Figure 3](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/Julia%20fig3%20Q1.jpg)

**Figure 3.** helps analyze geographical factors and estimated completion rates. I have presented this graph using District numbers which can be attributed to each matching District name, which provides the school's location in question. This data is incredibly valuable as it shows the estimated completion rates for each district. While lower does not mean not as successful, and we must consider the community's population. It is still interesting to view as it hints at the size of each district; assuming the majority of school-aged adolescents within each section are receiving an education, it can lead to conversations with the teenage population in that area.

#### The size or population of a cohort, how many students are in each one - all following the same curriculum.

![Figure 4](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/Julia%20fig4%20Q2.jpg)

**Figure 4.** visualizes the number of students in a cohort per year. Considering how many students are learning the same curriculum simultaneously is interesting. This graph answers my second research question regarding pure cohort sizes. In 1997/1998, the cohort size was considerably more significant than the cohort sizes in 2021; from this, I wonder what strategic choices are behind deciding cohorts and what benefits smaller cohorts have. Based on the data, smaller cohorts are the preferred method as the sizes do not reach anywhere close to the range that was 1997/1998. The data trends towards smaller cohort sizes, and 2020/2021 cohort is one of the smallest. These cohorts refer to grade eight and forward; I would have been considered within this data in the 2014/2015 cohort, which was slightly smaller than the year before and somewhat bigger than the year to follow, demonstrating the downward trend.

#### I want to gain a more extensive understanding of how cohorts work, how many students are in cohorts and if a cohort affects graduation or success rates in students. This ideology leads to my internal understanding of the school systems and their successes and flaws. If, while examining the data, I found a significant drop in a cohort's success rate, I may be able to attribute the decline to the format and content those students were learning or what world events were happening at that time.

![Figure 5](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/Julia%20fig5%20Q3.jpg)
**Figure 5** demonstrates the correlation. For the purpose of my research questions, I will focus mainly on those with the highest correlation - SUCCESS_COUNT and COHORT_COUNT. This data is the most interesting within the dataset as it considers whether the cohort is successful. SUCCESS_COUNT and COHORT_COUNT are 0.99 on the correlation scale and 0.1% from being identical. From this, I gather that the first is that most cohorts are successful, which makes sense considering my experience within high school and the attendance and population rates I personally experienced. Additionally, this graphic shows a low correlation between the district number and the estimated completion rates. Initially, I wondered if more rural areas (as determined by the district number, which is equal to the district name/area) would have lower estimated completion rates as those districts may have less access to funding than the larger populated districts. I am glad to discover that the community's position has little effect on the students' success.

#### I want to consider the estimated outmigrants as well and examine if there were periods of time when more students were leaving the school district than others.

![Figure 6](https://github.com/ubco-W2022T1-cosc301/project-group19/blob/main/images/Julia%20fig6%20Q4.jpg)
**Figure 6.** considers the number of students who left British Columbia during the school year and did not return before the school year ended. This data began with high levels of students departing or out-migrating at the beginning of the study/dataset. This number seemed to steady starting in the 2000s and only fluctuated slightly. The years tend to move gradually (Minus the date from the 1990s). 2020/2021 has the lowest outmigrants data of the set, which makes sense considering the COVID-19 Pandemic drastically limited the way British Columbians were able to move around the country. However, the numbers, even at most, remain relatively low regardless of highs or lows. Within the thousands of students within the British Columbia education system, the number of students departing remains relatively low, with this chart only needing to go to 400 on the X axis.
## Conclusion:

Acquiring a high school education is highly valued in our society and it has been interesting to analyze a dataset from the British Columbia Ministry of Education. According to our analysis, the school system has been improving throughout the years 1997-2021 regarding the increase of overall completion rates, as well as indigenous and students with disabilities completion rates. A school district’s population size has a positive relationship with its completion rate - on average, the higher the population of the school district, the higher the completion rate. Cohort size has decreased throughout the years, which may suggest that smaller cohorts are preferred and lead to a higher standard of education. Overall, the dataset we used raises some interesting talking points about the BC education system that our analysis could investigate.
