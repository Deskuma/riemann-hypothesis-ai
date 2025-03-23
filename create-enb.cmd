@echo off
echo Creating knowledge base...
python src/py/gpt/knowledge/create_knowledge.py -k knowledge-list.txt -d enb
echo Done.
