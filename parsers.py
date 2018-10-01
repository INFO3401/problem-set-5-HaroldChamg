1. Starbucks wants to evaluate whether their mobile pay solutions are having a positive impact on customer service. Outline how they might collect data to answer this question using:
An Observational Study:
	Starbucks can simply just observe their customers(in any of their store, and aiming at their rush hour, such as morning), see if more and more customers are using their mobile pay service. Besides, Starbucks can also record the time difference between using cash and using mobile pay, to compare if using mobile pay actually save their consumers time, if it does save some time, conclude how much time they save.
Question could be: Would mobile pay service actually saves time?
B. Focus Groups:
	I am only going to focus on ages between 15-55. This range of people are most active on smartphone, which is related to the chance the know mobile pay, you can’t expect categories that barely use smartphone to use the mobile pay app. Among the candidate between 15-55, aging between 16-23 is my main emphasis, because those ages represent as students who lean on coffee a lot, but meanwhile probably don’t have their own coffee machine. As result they will be a ultimate group for my group studies.

Questions could be: How often to teens used mobile pay compared to other ages?
	
	
C. An Online Survey:
	This is like the most straight forward method in my opinion. Starbucks designed a bunch of questions related to the usage of mobile pay service, and just see if the impact is positive. However, be very careful, because as my experiences before, survey is the least reliable source to rely on.

Question could be: Would you use online pay next time? Why?

2. In 2014, Facebook conducted their infamous Emotional Contagion study where they manipulated users' newsfeeds to contain differing amounts of positive and negative content. Name the (a) research question, (b) independent variables(different conditions needed to be testes out), and (c) dependent variables(things we wanna measure) that Facebook used in this study. 
1, Wether negative newsfeed receive more likes?
2, We need to test out how many comments received by both negative and positive newsfeed, and then compare which has high comments
3, We wanna measure the comments received by negative newsfeeds

3. What kind of data collection strategies would you use to:
Determine user perceptions of a social media campaign

	Focused group

B. Assess the effectiveness of a web redesign

	Survey
	
C. Decide whether the next iPhone will live up to its hype (and turn a profit)

	Documents and Records

		
	
4. For the three scenarios above, describe how you would conduct each investigation (i.e., not only the type of method, but what question would you answer, what procedure would you use, what kind of data would you collect, and how would you analyze that data to answer your question). 
1, The question i would ask is “How interactive are the users on this social media campaign?” I would access to the log-data behind the website and trying to see how interactive the users are on this campaign. For me, interaction can be anything like “How long did the users stay?”, “How many comments they posted on the campaign?”, or “If its on Facebook, would the users invited their friends or mutual friends to this event?” After collecting those data, I would be able to roughly tell users perception toward this campaign.
2,  As I mentioned before, the crucial problem that survey has to face is less reliability. However, I think in this scenario, it would be a lot better, because it is directly affecting the users. For example, if anyone wants to ask me my opinion toward “Canvas” compared to D2L, I would be very kindly to offer my thoughts, because that is something I will use daily. Therefore, the question I would ask is “From 1 to 5(most satisfied or effective), how will you grade our new system?” Then I will average the number see if its above 4.
3, To analyzing if the new product is going to be profitable or not, I would like to have all the records(data) from that company for those related products. This is the time we can apply machine learning, I will analyze Apple’s customers trend, and see the likelihood that buyers would purchase the newest product.

5. Describe how you might use data fusion to determine how the location people are in influences the ways they communicate with others. Assume you have full access to data from all technologies that a person may be carrying with them or that may be embedded in the environment. 

I think the the first thing that I’d be able to tell from data fusion is “Language”, different locations have their own languages, though more and more people start using English, yet there are still some area not apply English as their main language. Another thing is the population. Image the revenue in America will never be able to compare with revenue in Taiwan(small country where I originally came from). As a result, the result of the visualization will look very different. 



6. Format Parsing: Use the skeleton code in Problem_Set_5.zip to construct parsers to work with Unstructured, List, and Hierarchical data formats to analyze a text dataset. Directions are within the file. 
    
Source from: Stack over flow

def countWordsUnstructured(filename):
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    
# Test your part 1 code below.
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (wordcount)
(countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1990.txt'))
