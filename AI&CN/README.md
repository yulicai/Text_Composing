# A series of poems in responding to Ai Weiwei and Lego event


**I am not a big fan of Ai Weiwei.**
<br /><br />
I went to couple of his exhibitions before, I see the way he is doing art is too intentional in which has too much rage. I remember it clearly that I was watching a documentary film of him trying to convey the message that Chinese government is acting like a dictator and is not liberal. But in the movie, I actually saw a bully as him, trying to push the silent officer to get something out of his mouth or push the officer to act back badly to prove the his message. That makes me feel uncomfortable.
<br />
<br />
And it seems reasonable that he is such a big artist in the western world for his criticism toward Chinese government.
<br /><br />
Recently there was a thing that he wants to use Lego’s bricks to build portrait of those who are prisoned for some reason. But Lego refused to sell it directly to him because they have a policy that would not let their product to be used for a political purpose.
<br /><br />
And then, I think it is started by Brooklyn Museum, which raised an action on instagram as #legoforweiwei to help him collect enough Lego bricks, which raised this huge debate about Lego’s act.
<br />

<img src = "https://github.com/yulicai/Text_Composing/raw/master/images/result_all_text.png" width = "500">

<img src = "https://github.com/yulicai/Text_Composing/raw/master/images/result_nytimes.png" width = "500">

##How I generate the poem

I scrape two articles on line, one from [New York Times titled Art Man of Alcatraz](https://www.nytimes.com/2014/09/21/arts/design/ai-weiwei-takes-his-work-to-a-prison.html), another from [BBC titled Lego changes bulk buy policy after Ai Weiwei backlash](http://www.bbc.com/news/world-35299069). Using them as the source text, I create these two computer generated poems.

**Conceptually it is generated as following steps:**
<br />
**1. scrape the source text**
<br />
**2. using python library TextBlob to take the verb, noun and adjective words from the source text**
<br />
**3. using word count method to get the most common 40 words for each category.**
<br />
**4. randomly select 10 words from each and place them in this order: Aiweiwei claims Verb Adjective Noun, Chinese government says Verb Adjective Noun. So every time I run the program it will give me a new poem**
