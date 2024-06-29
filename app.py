
import tkinter as tk

from src.helpers import set_background, clear_widgets


root = tk.Tk()
root.title("GymGirls")
root.geometry("430x530")

#reference:https://github.com/shaq31415926/python_tech_basics/blob/main/tech_basics_two/13Lecture/app.py
#returns to home page "hi gymgirl" once you have set up your profile
def new_page_setup(root):

    # this clear all the widgets that have been created
    clear_widgets(root)

    # add a home page button - this will go back to our home page
    homepage = tk.Button(root,
                         text="🏠",
                         command=lambda: gymgirl_homepage(root)
                         )
    homepage.place(relx=0.4, rely=0.92)

# creates exit button
def exit_button(root):
    exit_button = tk.Button(text="X",
                            font=("Comic Sans MS", 14, "bold"),
                            fg= "red",
                            bg="grey",
                            command=root.destroy
                            )
    exit_button.grid(column=0, row=4, padx=10, pady=10)
    exit_button.place(relx=0.85,
                      rely=0.925)

# login frame to put in username and password
def login_frame(root):

    #main background "women for women"
    set_background(root, "images/homepage_background.png", width= 430, height=530)

    exit_button(root)

    # Widgets for the first frame
    # creates username and password label
    # sets font
    # creates entry boxes for username and password

    label_username = tk.Label(root, text="Username:", fg="VioletRed3", font=("Helvetica", 22), bg="white")
    label_username.place(relx=0.1, rely=0.2)

    entry_username = tk.Entry(root)
    entry_username.place(relx=0.4, rely=0.2)

    label_password = tk.Label(root, text="Password:", fg="VioletRed3", font=("Helvetica", 22), bg="white")
    label_password.place(relx=0.1, rely=0.4)

    # shows * instead of letters for password
    entry_password = tk.Entry(root, show="*")
    entry_password.place(relx=0.4, rely=0.4)

    # Creates a button to join gym girls and leads to welcome frame
    join_button = tk.Button(root, text="Join GymGirls", font=("Helvetica", 22), command=lambda: welcome_frame(root))
    join_button.place(relx=0.3, rely=0.6)

# welcome frame
def welcome_frame(root):
    clear_widgets(root)

    exit_button(root)

    set_background(root, "images/homepage_background.png", width= 430, height=530)

    exit_button(root)

    # Widgets for the welcome frame
    label_welcome = tk.Label(root, text="Welcome to GymGirls!", fg="VioletRed2", font=("georgia", 26), bg='#FFE1FF')
    label_welcome.place(relx=0.15, rely=0.3)

    # leads to membership frame
    profile_button = tk.Button(root, text="Tell us about your membership status",font=("Helvetica", 22), command=lambda: membership_frame(root))
    profile_button.place(relx=0.02, rely=0.5)

    # leads back to login frame
    Back_to_login_Button = tk.Button(root, text="⬅️", command=lambda: login_frame(root))
    Back_to_login_Button.place(relx=0.1, rely=0.92)

# frame for entering membership status
def membership_frame(root):

    clear_widgets(root)

    # pink background
    root.configure(background="#FFE1FF")

    exit_button(root)

    # Widgets for the membership frame
    label_profile = tk.Label(root, text="Membership Status", font=("Helvetica", 20))
    label_profile.place(relx=0.2,rely=0)

    label_membership = tk.Label(root, text="Gym Membership:",font=("Helvetica", 16) )
    label_membership.place(relx=0,rely=0.3)

    # dropdown menu for membership status
    # reference https://www.geeksforgeeks.org/dropdown-menus-tkinter/
    membership_options = ["Yes", "No"]
    var_membership = tk.StringVar(root)
    var_membership.set(membership_options[0])  # Default value
    dropdown_membership = tk.OptionMenu(root, var_membership, *membership_options)
    dropdown_membership.place(relx=0.4,rely=0.3)

    label_yes_no = tk.Label(root, text="if yes which one:",font=("Helvetica", 16))
    label_yes_no.place(relx=0,rely=0.4)

    entry_yes_no = tk.Entry(root)
    entry_yes_no.place(relx=0.4,rely=0.4)

    label_goals = tk.Label(root, text="Fitness Goals:", font=("Helvetica", 16))
    label_goals.place(relx=0,rely=0.5)

    entry_goals = tk.Entry(root)
    entry_goals.place(relx=0.4,rely=0.5)

    # Adds a button to save the profile
    # leads to next frame
    save_button = tk.Button(root, text="Save", font=("Helvetica", 20), command=lambda: saved_profile_frame(root))
    save_button.place(relx=0.4,rely=0.75)

    Back_to_welcome_Button = tk.Button(root, text="⬅️", command=lambda: welcome_frame(root))
    Back_to_welcome_Button.place(relx=0.1, rely=0.92)

# frame "get started"
def saved_profile_frame(root):

    clear_widgets(root)

    exit_button(root)

    root.configure(background="#FFE1FF")

    # widgets for membership saved frame
    label_saved_profile = tk.Label(root, text="Membership Saved!", fg="VioletRed2", font=("georgia", 26), bg='#FFE1FF')
    label_saved_profile.place(relx=0.25,rely=0.3)

    # leads to next frame
    button_getstarted = tk.Button(root, text="Get started", font=("Helvetica", 26), command=lambda: gymgirl_homepage(root))
    button_getstarted.place(relx=0.27,rely=0.5)

    #leads back to last frame
    Back_to_create_profile_Button = tk.Button(root, text="⬅️", command=lambda: membership_frame(root))
    Back_to_create_profile_Button.place(relx=0.1, rely=0.92)

# this is the central hub of gymgirls
# homepage with main funtions: profile, about gymgirls, connect, share
def gymgirl_homepage(root):

    clear_widgets(root)

    set_background(root, "images/homepage_background.png", width=430, height=530)
    exit_button(root)

    root.configure(background="#FFE1FF")

    label_welcome = tk.Label(root, text="Hi GymGirl!", fg="VioletRed2", font=("georgia", 26), bg='#FFE1FF')
    label_welcome.place(relx=0.3,rely=0.1)

    # Adds buttons for main functions

    # more info about gymgirl and its aim
    about_gym_girls_button = tk.Button(root, text="About GymGirls", font=("georgia",24), command=lambda: about_us(root))
    about_gym_girls_button.place(relx=0.2,rely=0.3)

    # opens map
    connect_button = tk.Button(root, text="Connect with Gym Girls", font=("georgia",24),command=lambda: connect_with_gym_girls(root))
    connect_button.place(relx=0.17,rely=0.5)

    # share
    share_button = tk.Button(root, text="Share Experiences",font=("georgia",24), command=lambda: share_experiences(root))
    share_button.place(relx=0.2,rely=0.7)

    # here the user can create their profile
    profile_button= tk.Button(root, text="👤 Your Profile", command=lambda:user_profile(root))
    profile_button.place(relx=0.7,rely=0.05)

    # leads back to membership frame
    Back_to_save_profile_Button = tk.Button(root, text="⬅️", command=lambda: membership_frame(root))
    Back_to_save_profile_Button.place(relx=0.1, rely=0.92)

# asked chatgpt for help here
# how to transfer entries from user_profile to Your_saved_profile

#profile data
def save_profile(root, profile_data):
    profile_data["name"] = entry_name.get()
    profile_data["age"] = entry_age.get()
    profile_data["experience"] = var_experience.get()
    profile_data["training"] = entry_training.get()
    profile_data["why"] = entry_why.get()
    profile_data["contact"] = entry_contact.get()
    profile_data["cycle"] = var_cycle.get()
    Your_saved_Profile(root, profile_data)

# here user can enter more detailed information
# fill out gymgirl blank form
def user_profile(root):
    profile_data = {}  # Dictionary to store user profile data

    new_page_setup(root)
    root.configure(background="pink1")

    # Widgets for the profile frame
    label_profile = tk.Label(root, text="Tell Them About You ", fg="DeepPink4", font=("Helvetica", 20 ))
    label_profile.place(relx=0.2, rely=0)

    global entry_name, entry_age, var_experience, entry_training, entry_why, entry_contact, var_cycle

    # Add profile labels and input fields
    label_name = tk.Label(root, text="Name:", font=("Helvetica", 16))
    label_name.place(relx=0, rely=0.1)
    entry_name = tk.Entry(root)
    entry_name.place(relx=0.4, rely=0.1)

    label_age = tk.Label(root, text="Age:", font=("Helvetica", 16))
    label_age.place(relx=0, rely=0.2)
    entry_age = tk.Entry(root)
    entry_age.place(relx=0.4, rely=0.2)

    #dropdown menu
    label_experience = tk.Label(root, text="Experience", font=("Helvetica", 16))
    label_experience.place(relx=0, rely=0.3)
    experience_options = ["New Here", ">6 months", "<6 months", "1 Year", "2 Years", "<2 Years"]
    var_experience = tk.StringVar(root)
    var_experience.set(experience_options[0])  # Default value
    dropdown_experience = tk.OptionMenu(root, var_experience, *experience_options)
    dropdown_experience.place(relx=0.4, rely=0.3)

    label_training = tk.Label(root, text="Training Plan/Interested in", font=("Helvetica", 13))
    label_training.place(relx=0, rely=0.4)
    entry_training = tk.Entry(root)
    entry_training.place(relx=0.4, rely=0.4)

    label_why = tk.Label(root, text="Why GymGirls?", font=("Helvetica", 16))
    label_why.place(relx=0, rely=0.5)
    entry_why = tk.Entry(root)
    entry_why.place(relx=0.4, rely=0.5)

    label_contact = tk.Label(root, text="Contact me via:", font=("Helvetica", 16))
    label_contact.place(relx=0, rely=0.6)
    entry_contact = tk.Entry(root)
    entry_contact.place(relx=0.4, rely=0.6)

    label_cycle = tk.Label(root, text="Day of your Cycle", font=("Helvetica", 16))
    label_cycle.place(relx=0, rely=0.7)
    cycle_options = ["1-7", "8-14", "15-21", "22-28"]
    var_cycle = tk.StringVar(root)
    var_cycle.set(cycle_options[0])  # Default value
    dropdown_cycle = tk.OptionMenu(root, var_cycle, *cycle_options)
    dropdown_cycle.place(relx=0.4, rely=0.7)

    # Adds a button to save the profile
    # leads to saved profile
    save_button = tk.Button(root, text="Save", font=("Helvetica", 20),
                            command=lambda: save_profile(root, profile_data))
    save_button.place(relx=0.38, rely=0.8)

    home_button = tk.Button(root, text="🏠", command=lambda: gymgirl_homepage(root))
    home_button.place(relx=0.4, rely=0.92)

# filled out form with info you put in in frame before
def Your_saved_Profile(root, profile_data):
    new_page_setup(root)

    set_background(root, "images/Empty_Profile.png", width=430, height=530)

    # Display saved profile information
    root.configure(background="pink1")

    label_saved = tk.Label(root, text="Your Saved Profile", fg="DeepPink4", font=("Helvetica", 20))
    label_saved.place(relx=0.3, rely=0.0)

    label_name = tk.Label(root, text=f" {profile_data['name']}", font=("Helvetica", 16))
    label_name.place(relx=0.6, rely=0.2)

    label_age = tk.Label(root, text=f" {profile_data['age']}", font=("Helvetica", 16))
    label_age.place(relx=0.23, rely=0.42)

    label_experience = tk.Label(root, text=f" {profile_data['experience']}", font=("Helvetica", 16))
    label_experience.place(relx=0.7, rely=0.3)

    label_training = tk.Label(root, text=f" {profile_data['training']}", font=("Helvetica", 16))
    label_training.place(relx=0.45, rely=0.5)

    label_why = tk.Label(root, text=f" {profile_data['why']}", font=("Helvetica", 16))
    label_why.place(relx=0.1, rely=0.55)

    label_contact = tk.Label(root, text=f" {profile_data['contact']}", font=("Helvetica", 16))
    label_contact.place(relx=0.1, rely=0.85)

    label_cycle = tk.Label(root, text=f" {profile_data['cycle']}", font=("Helvetica", 16))
    label_cycle.place(relx=0.45, rely=0.8)

    home_button = tk.Button(root, text="🏠", command=lambda: gymgirl_homepage(root))
    home_button.place(relx=0.4, rely=0.92)

    Back_to_profile_Button = tk.Button(root, text="⬅️", command=lambda: user_profile(root))
    Back_to_profile_Button.place(relx=0.1, rely=0.92)

# more information about what gymgirls aims to do
def about_us(root):
    new_page_setup(root)

    #designed with canva
    set_background(root,"images/About_GymGirls.png", width= 430, height=530)

    # shifted home button to the side for design reasons
    home_button = tk.Button(root, text="🏠",command=lambda: gymgirl_homepage(root))
    home_button.place(relx=0.8, rely=0.92)

# opens hamburg map with three example gym locations
def connect_with_gym_girls(root):

    set_background(root, "images/gyms_near_me.png", width= 430, height=530)

    # pins for locations
    pin1_button = tk.Button(root, text="📍",font= 24, command=lambda: Gym_A(root))
    pin1_button.place(relx=0.5,
                      rely=0.7,
                      )

    pin2_button = tk.Button(root, text="📍",font= 24, command=lambda: Gym_B(root))
    pin2_button.place(relx=0.2,
                      rely=0.4,
                      )

    pin3_button = tk.Button(root, text="📍", font= 24,command=lambda: Gym_C(root))
    pin3_button.place(relx=0.7,
                      rely=0.3,
                      )

    home_button = tk.Button(root, text="🏠", command=lambda: gymgirl_homepage(root))
    home_button.place(relx=0.4, rely=0.92)

# Gym A "Fitness St.Georg"
# 2 example profiles "Lisa B." and "Sarah M."
def Gym_A(root):
    new_page_setup(root)

    label_Gym_A = tk.Label(root, text="Fitness St.Georg", font=("Helvetica", 16))
    label_Gym_A.place(relx=0.3,rely=0)

    Lisa_B_Button = tk.Button(root, text="Get to know Lisa B.", command=lambda:Lisa_B_profile(root))
    Lisa_B_Button.place(relx=0.1, rely=0.2)

    Sarah_M_Button = tk.Button(root, text="Get to know Sarah M.", command=lambda:Sarah_M_profile(root))
    Sarah_M_Button.place(relx=0.1, rely=0.3)

    #leads back to map
    Back_to_Map_Button = tk.Button(root, text= "Back to Map", command=lambda:connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

# Profile of Lisa B.
def Lisa_B_profile(root):
    new_page_setup(root)

    # designed the forms with canva
    set_background(root, "images/Lisa_B.png", width= 500, height=650 )

    #back to map
    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

    #leads back to profiles available at this location
    Back_to_Gym_A_Button = tk.Button(root, text="⬅️", command=lambda:Gym_A(root))
    Back_to_Gym_A_Button.place(relx=0.1,rely=0.92)

#profile of Sarah M.
def Sarah_M_profile(root):
    new_page_setup(root)

    # designed with canva
    set_background(root, "images/Sarah_M.png", width= 500, height=650)

    #back to map
    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

    #back to profiles available at this location
    Back_to_Gym_A_Button = tk.Button(root, text="⬅️", command=lambda: Gym_A(root))
    Back_to_Gym_A_Button.place(relx=0.1, rely=0.92)

# Gym B "Fitness Eimsbüttel"
def Gym_B(root):
    new_page_setup(root)

    label_Gym_B = tk.Label(root, text="Fitness Eimsbüttel", font=("Helvetica", 16))
    label_Gym_B.place(relx=0.3, rely=0)

    Lily_S_Button = tk.Button(root, text="Get to know Lily S.", command=lambda: Lily_S_profile(root))
    Lily_S_Button.place(relx=0.1, rely=0.2)

    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

    Back_to_Gym_B_Button = tk.Button(root, text="⬅️", command=lambda: Gym_B(root))
    Back_to_Gym_B_Button.place(relx=0.1, rely=0.92)

# profile of Lily S.
def Lily_S_profile(root):
    new_page_setup(root)

    # designed with canva
    set_background(root, "images/Lily_S.png", width= 500, height=650)

    #back to map
    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

    #back to profiles available at this location
    Back_to_Gym_B_Button = tk.Button(root, text="⬅️", command=lambda: Gym_B(root))
    Back_to_Gym_B_Button.place(relx=0.1, rely=0.92)

#Gym C "Fitness Barmbek"
def Gym_C(root):
    new_page_setup(root)

    label_Gym_C = tk.Label(root, text="Fitness Barmbek", font=("Helvetica", 16))
    label_Gym_C.place(relx=0.3, rely=0)

    label_no_users = tk.Label(root, text="No GymGirls yet ☹️", font=("Helvetica", 20))
    label_no_users.place(relx=0.2, rely=0.1)

    label_tell_your_friends = tk.Label(root, text="Tell Your Friends About Us!!!!️", font=("Helvetica", 20))
    label_tell_your_friends.place(relx=0.15, rely=0.2)

    #back to map
    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

# opens chat to share experiences
# got this code from the 11lecture/simple_chatbot.py and adjusted a few things
def share_experiences(root):

    new_page_setup(root)

    welcome_label = tk.Label(root,
                             text="Share Your Experiences",fg="VioletRed2", font=("georgia", 26))
    welcome_label.place(relx=0.2,rely=0)

    text_box = tk.Text(root,
                       width=60)
    text_box.place(x=0, y=30, relwidth=1, relheight=1)

    scroll_bar = tk.Scrollbar(text_box)
    scroll_bar.place(relheight=1,
                     relx=0.974)

    entry_box = tk.Entry(root,
                         width=55
                         )
    entry_box.place(x=5,
                    rely=0.925)

    send_button = tk.Button(root,
                            text="Send",
                            command=lambda: send(root),
                            width=10)
    send_button.place(relx=0.77,
                      rely=0.925)

# opens frame to say thank you for sharing
def send(root):

    new_page_setup(root)
    thank_you_label = tk.Label(root,
                               text="Thank You For Sharing ♥️",
                               fg="VioletRed2",
                               font=("georgia", 26),
                               bg='#FFE1FF')
    thank_you_label.place(relx=0.2,rely=0.5)


login_frame(root)

root.mainloop()
