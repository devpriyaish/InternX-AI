from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-5")

topic = input("Enter topic: ")
number_of_lines = input("Enter number of lines: ")
style = input("Enter style: ")
language = input("Enter language: ")
print()
system_prompt = f"You are a helpful litrature assistant. You need to answer the questions in {style} form and in {number_of_lines} lines only about topic {topic}. Response in only {language} language. Analyze your answer before printing it."

result =cm.invoke(system_prompt)

print(result.content)


# धरती-जल-पवन के भेद, पूछो भूगोल विचार;
# पर्वत, सागर, मरु-वन संग, रचे प्रकृति के द्वार।
# प्रश्न धरो मन साफ कर, जानो जग की तसवीर—
# चार पंक्तियों में कहूँ सत्य, कहै कबीर गम्भीर।

# धन (Money) विनिमय का माध्यम, मूल्य का संचय और लेखा की इकाई है, जिससे लेन-देन कुशल, मानकीकृत और विश्वसनीय बनते हैं। 
# साहित्य और समाज में यह शक्ति, असमानता व आकांक्षाओं का प्रतीक भी है; अतः इसके अर्जन-व्यय में नैतिकता, जोखिम-संतुलन और दीर्घकालिक दृष्टि आवश्यक हैं।