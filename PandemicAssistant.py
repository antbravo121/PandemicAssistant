import streamlit as st
from GoogleAPI import get_results
from CovidML import get_predict
from PIL import Image

#Init sidebar (navigation bar)
st.sidebar.write("# Navigation")
page = st.sidebar.radio("Go to",["Home", "Item Finder","Symptoms Checker"])
image0 = Image.open('mask.jpg')
st.sidebar.image(image0, use_column_width=True)


def Home_Page():
	st.write("# Pandemic Assistant")
	st.write("Welcome to the Pandemic Assistant web app, here you have access to a few tools to improve your time during the pandemic! :smile:")
	st.write("On the side is a Navigation Bar where you can switch between the different tools. ")
	st.write("The Item Finder helps you find stores that are selling items that may be hard to find during the pandemic.")
	st.write("The Symptoms Checker is a questionarrie that determines whether you are at a high risk of having COVID-19 or not. This program should uses a Nearest Neighbor Classifer that predicts with a 97% accuracy.")
	image1 = Image.open('fightcorona.jpg')
	st.image(image1, use_column_width=True)

def Items_Finder_Page():
	st.write("# Item Finder")
	col1, col2, col3 = st.beta_columns(3)
	with col1:
		item_input = st.selectbox('Pick an item to search',
			('Masks', 'Hand Sanitizers', 'Hand Soap', 'Disposable Gloves', 'Disinfectant Wipes'))

	with col2:
		 location_to_search = st.text_input("Enter City (ex: Dallas)")

	with col3:
		search_btn = st.button("Click to Search")

	#changes item input into one word so api can work correctly
	item_to_search = ""
	if item_input == "Masks":
		item_to_search = "Masks"
	elif item_input == "Hand Sanitizers":
		item_to_search = "Hand_Sanitizers"
	elif item_input == "Hand Soap":
		item_to_search = "Soap"
	elif item_input == "Disposable Gloves":
		item_to_search = "Disposable_Gloves"
	elif item_input == "Disinfectant Wipes":
		item_to_search = "Disinfectant_Wipes"


	if search_btn:
		items_to_display = get_results(item_to_search, location_to_search)
		for item in items_to_display:
			#draw title
			if item.title != None:
				st.write("### {}".format(item.title))
			else:
				st.write("")
			#draw source
			if item.source != None:
				st.write("###### by: {}".format(item.source))
			else:
				st.write("")
			#draw price
			if item.price != None:
				st.write("{}".format(item.price))
			else:
				st.write("")
			#draw link
			if item.link != None:
				st.markdown("[{}]({})".format("Link", item.link))
			else:
				st.write("")
			#draw seperator
			st.write("---")
	


def Symptoms_Checker_Page():
	st.write("# COVID-19 Symptoms Checker")
	features = 20*[""]

	st.write("Answer the following questions and then press calculate. :mask:")
	image = Image.open('pic1.jpeg')
	st.image(image, use_column_width=True)
	st.write("---")

	st.write("Do you have any of the following symptoms? Please select all that apply.")
	if st.checkbox('Trouble Breathing'):
		features[0] = 1
	else:
		features[0] = 0

	if st.checkbox('Fever'):
		features[1] = 1
	else:
		features[1] = 0

	if st.checkbox('Dry Cough'):
		features[2] = 1
	else:
		features[2] = 0

	if st.checkbox('Sore Throat'):
		features[3] = 1
	else:
		features[3] = 0

	if st.checkbox('Runny Nose'):
		features[4] = 1
	else:
		features[4] = 0

	if st.checkbox('Headache'):
		features[7] = 1
	else:
		features[7] = 0

	if st.checkbox('Fatigue'):
		features[11] = 1
	else:
		features[11] = 0

	st.write("Have you been diagnosed with any of the following condition or conditions? Please select all that apply.")
	if st.checkbox('Heart Disease'):
		features[8] = 1
	else:
		features[8] = 0

	if st.checkbox('Asthma'):
		features[5] = 1
	else:
		features[5] = 0

	if st.checkbox('Chronic Lung Disease'):
		features[6] = 1
	else:
		features[6] = 0

	if st.checkbox('Diabetes'):
		features[9] = 1
	else:
		features[9] = 0
	
	if st.checkbox('Hyper Tension'):
		features[10] = 1
	else:
		features[10] = 0

	if st.checkbox('Gastrointestinal'):
		features[12] = 1
	else:
		features[12] = 0

	st.write("Please select all that apply.")
	if st.checkbox('Traveled'):
		features[13] = 1
	else:
		features[13] = 0

	if st.checkbox('Came in contact with a COVID-19 patient'):
		features[14] = 1
	else:
		features[14] = 0

	if st.checkbox('Attended a large gathering'):
		features[15] = 1
	else:
		features[15] = 0

	if st.checkbox('Visited public exposed places'):
		features[16] = 1
	else:
		features[16] = 0

	if st.checkbox('Family working in public exposed places'):
		features[17] = 1
	else:
		features[17] = 0

	if st.checkbox('Wearing masks'):
		features[18] = 1
	else:
		features[18] = 0

	if st.checkbox('Sanitization from market'):
		features[19] = 1
	else:
		features[19] = 0

	done_btn = st.button("Press to calculate")

	if done_btn:
		result = get_predict(features)
		if result == 0:
			st.write("### You have a **Low** risk :smile:")
			st.write("You don't have to get tested immediately")
		else:
			st.write("### You have a **High** risk :face_with_thermometer:")
			st.write("You should get tested immediately")

#Change page when selected
if page == "Home":
	Home_Page()
elif page == "Item Finder":
	Items_Finder_Page()
elif page == "Symptoms Checker":
	Symptoms_Checker_Page()
