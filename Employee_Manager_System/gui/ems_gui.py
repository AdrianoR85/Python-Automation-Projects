from customtkinter import *
from util.window_utils import center_window, get_image, setup_window
from config.setting import WINDOW_EMS, COLORS, COMPONENT_CONFIG, FONTS
from data.role import role_options, gender_options, search_options
from data.models import Employee
from tkinter import ttk, messagebox
from services.employee_service import EmployeeService

class ManagementSystemGUI(CTk):
  def __init__(self, conn):
    super().__init__()
    self.conn = conn
    self._main_window()
    self._widgets()

    self.protocol("WV_DELETE_WINDOW", self._on_close)
  
 # WINDOW CONFIGURATION
  def _main_window(self):
    setup_window(self, WINDOW_EMS, COLORS['bg_secondary'])
    center_window(self)
    self._create_banner()

  def _create_banner(self):
    if get_image('banner'):
      image = get_image('banner')
      banner = CTkImage(image, size=(WINDOW_EMS['width'], WINDOW_EMS['banner_height'])) # type: ignore
      banner_label = CTkLabel(self, image=banner, text="")
      banner_label.grid(row=0, column=0, columnspan=2)
    else:
      self.configure(fg_color=COLORS['secondary'])
    
  def _widgets(self):
    self._left_frame()
    self._right_frame()
    self._button_frame()


# FRAMES 
  def _left_frame(self):
    self.left_frame = CTkFrame(self, fg_color=COLORS['bg_secondary'])
    self.left_frame.grid(row=1, column=0)

    # ID
    self.id_label = CTkLabel(
      self.left_frame, text='id', 
      font=FONTS['label'], 
      text_color=COLORS['text_light']
    )
    self.id_label.grid(row=0, column=0, padx=20, pady=15, stick='w')

    self.id_entry = CTkEntry(
      self.left_frame, 
      width=COMPONENT_CONFIG['small_entry_width'], 
      height=COMPONENT_CONFIG['small_entry_height'],
      font=FONTS['entry']
    )
    self.id_entry.grid(row=0, column=1)

    # Name
    self.name_label = CTkLabel(
      self.left_frame, 
      text='name', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.name_label.grid(row=1, column=0, padx=20, pady=15, stick='w')

    self.name_entry = CTkEntry(
      self.left_frame, 
      width=COMPONENT_CONFIG['small_entry_width'], 
      height=COMPONENT_CONFIG['small_entry_height'],
      font=FONTS['entry']
    )
    self.name_entry.grid(row=1, column=1)

    # Phone
    self.phone_label = CTkLabel(
      self.left_frame, 
      text='Phone', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.phone_label.grid(row=2, column=0, padx=15, pady=15, stick='w')

    self.phone_entry = CTkEntry(
      self.left_frame, 
      width=COMPONENT_CONFIG['small_entry_width'], 
      height=COMPONENT_CONFIG['small_entry_height'],
      font=FONTS['entry']
    )
    self.phone_entry.grid(row=2, column=1)

    # Role
    self.role_label = CTkLabel(
      self.left_frame, 
      text='Role', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.role_label.grid(row=3, column=0, padx=15, pady=15, stick='w')

    self.role_box = CTkComboBox(
      self.left_frame, 
      width=COMPONENT_CONFIG["small_entry_width"], 
      height=COMPONENT_CONFIG["small_entry_height"],
      values=role_options,
      state="readonly",
      font=FONTS['entry']
    )
    self.role_box.grid(row=3, column=1)
    self.role_box.set(role_options[0])

    # Gender
    self.gender_label = CTkLabel(
      self.left_frame, 
      text='Gender', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.gender_label.grid(row=4, column=0, padx=15, pady=15, stick='w')

    self.gender_box = CTkComboBox(
      self.left_frame, 
      width=COMPONENT_CONFIG["small_entry_width"], 
      height=COMPONENT_CONFIG["small_entry_height"],
      values=gender_options,
      state="readonly",
      font=FONTS['entry']
    )
    self.gender_box.grid(row=4, column=1)
    self.gender_box.set(gender_options[0])

    # Salary
    self.salary_label = CTkLabel(
      self.left_frame, 
      text='Salary', 
      font=FONTS['label'],
      text_color=COLORS['text_light']
    )
    self.salary_label.grid(row=5, column=0, padx=15, pady=15, stick='w')

    self.salary_entry = CTkEntry(
      self.left_frame, 
      width=COMPONENT_CONFIG["small_entry_width"], 
      height=COMPONENT_CONFIG["small_entry_height"],
      font=FONTS['entry']
    )
    self.salary_entry.grid(row=5, column=1)

  def _right_frame(self):
    self.right_frame = CTkFrame(self)
    self.right_frame.grid(row=1, column=1)

    self.search_box = CTkComboBox(
      self.right_frame, 
      width=150, 
      values=search_options, # type: ignore   
      state="readonly") 
    self.search_box.grid(row=0, column=0)
    self.search_box.set(search_options[0])
    self.search_box.set("Search By")

    self.search_name_entry = CTkEntry(self.right_frame, width=200)
    self.search_name_entry.grid(row=0, column=1)

    self.search_button = CTkButton(self.right_frame, text="Search", width=120)
    self.search_button.grid(row=0, column=2, pady=5)

    self.showall_button = CTkButton(self.right_frame, text="Show All", width=120)
    self.showall_button.grid(row=0, column=3, pady=5)

    self.tree = ttk.Treeview(self.right_frame, height=13)
    self.tree.grid(row=1, column=0, columnspan=4)
    self.tree['columns'] = search_options

    self.tree.heading(search_options[0], text=search_options[0])
    self.tree.heading(search_options[1], text=search_options[1])
    self.tree.heading(search_options[2], text=search_options[2])
    self.tree.heading(search_options[3], text=search_options[3])
    self.tree.heading(search_options[4], text=search_options[4])
    self.tree.heading(search_options[5], text=search_options[5])
    

    self.tree.config(show='headings')

    self.tree.column(search_options[0], width=80)
    self.tree.column(search_options[1], width=160)
    self.tree.column(search_options[2], width=130)
    self.tree.column(search_options[3], width=160)
    self.tree.column(search_options[4], width=90)
    self.tree.column(search_options[5], width=90)
    
    self._treeview_data()

    self.tree.bind("<Double-1>", self._on_item_double_click)

  def _button_frame(self):
    self.btn_frame = CTkFrame(self, fg_color=COLORS['bg_secondary'])
    self.btn_frame.grid(row=2, column=0, columnspan=2 )

    self.new_button = CTkButton(
      self.btn_frame, 
      text="New Employee", 
      font=FONTS['button'], 
      width=160,
      corner_radius=15,
      command=self._clean)
    self.new_button.grid(row=0, column=0, padx=10, pady=20)

    self.add_button = CTkButton(
      self.btn_frame, 
      text="Add Employee", 
      font=FONTS['button'], 
      width=160,
      corner_radius=15, 
      command=self._add_employee)
    self.add_button.grid(row=0, column=1, padx=10, pady=20)

    self.update_button = CTkButton(
      self.btn_frame, 
      text="Update Employee", 
      font=FONTS['button'], 
      width=160,
      corner_radius=15,
      command=self._update_employee)
    self.update_button.grid(row=0, column=2, padx=10, pady=20)

    self.delete_button = CTkButton(
      self.btn_frame, 
      text="Delete Employee", 
      font=FONTS['button'], 
      width=160,
      corner_radius=15,
      command=self._delete_one_employee )
    self.delete_button.grid(row=0, column=3, padx=10, pady=20)

    self.delete_all_button = CTkButton(
      self.btn_frame, 
      text="Delete All", 
      font=FONTS['button'], 
      width=160,
      corner_radius=15,
      command=self._delete_all_employee )
    self.delete_all_button.grid(row=0, column=4, padx=10, pady=20)

    self.scrollbar= ttk.Scrollbar(self.right_frame, orient=VERTICAL)
    self.scrollbar.grid(row=1, column=4, sticky='ns')


# INSERT, UPDATE AND DELETE
  def _add_employee(self):
    employee_data = self._get_data()

    if employee_data:
      try:
        EmployeeService.add_employee(employee_data, self.conn)
        messagebox.showinfo("Succeful", f"New employee has been created")
        self._treeview_data()
        
      except Exception as e:
        messagebox.showerror("Erro", f"Failed to create a new employee: {e}")
    else:  
        messagebox.showerror("Error", "All fields are required.")
    
  def _update_employee(self):
    employee = self._get_data(include_id=True)

    if employee:
      try:
        EmployeeService.update_employee(employee, self.conn)
        messagebox.showinfo("Succefull", f"Employee was updated!")
        self._treeview_data()
      except TypeError as e:
        print(e)
        messagebox.showerror("Error", f"The data type is wrong! {e}")
      except Exception as e:
        messagebox.showerror("Failed","Update not completed!")
    else:
      messagebox.showerror("Error", "All fields are required!")

  def _delete_one_employee(self):
    ...

  def _delete_all_employee(self):
    ...
  

  # DISPLAY THE INFORMATION ON THE SCREEM
  def _treeview_data(self):
    employees = EmployeeService.list_employee(self.conn)
    self.tree.delete(*self.tree.get_children())
    for employee in employees:
      self.tree.insert('', END, values=employee)
  

  # CLEAN THE FIELDS
  def _clean(self):
    self.id_entry.delete(0, END)
    self.name_entry.delete(0,END)
    self.phone_entry.delete(0,END)
    self.role_box.set(role_options[0])
    self.gender_box.set(gender_options[0])
    self.salary_entry.delete(0,END)
  

  # SELECTED A EMPLOYEE WHEN YOU DOUBLE CLICK ON THE EMPLOYEE
  def _on_item_double_click(self, event):
    selected = self.tree.focus()
    if selected:
        values = self.tree.item(selected, "values")
        self.id_entry.delete(0, "end")
        self.id_entry.insert(0, values[0])

        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, values[1])

        self.phone_entry.delete(0, "end")
        self.phone_entry.insert(0, values[2])

        self.role_box.set(values[3])
        self.gender_box.set(values[4])

        self.salary_entry.delete(0, "end")
        self.salary_entry.insert(0, values[5])
  

  # CLOSE THE CONNECTION WHEN THE WINDOW IS CLODED
  def _on_close(self):
    if self.conn:
      try:
        self.conn.close()
        print("Database connection has been closed.")
      except Exception as e:
        print(f"Failed to try close the connection: {e}")
    
    self.destroy()


  # GET ALL INFORMARION FROM AN EMPLOYEE
  def _get_data(self, include_id: bool = False):
      name = self.name_entry.get().strip()
      phone = self.phone_entry.get().strip()
      role = self.role_box.get().strip()
      gender = self.gender_box.get().strip()
      salary_str = self.salary_entry.get().strip()

      # Validação de campos obrigatórios
      if not name or not phone or not salary_str:
          messagebox.showerror("Error", "All fields are required.")
          return None

      # Validação do salário
      try:
          salary = float(salary_str)
      except ValueError:
          messagebox.showerror("Error", "Salary must be a number.")
          return None

      emp = Employee(
          name=name,
          phone=phone,
          role=role,
          gender=gender,
          salary=salary
      )

      # Se for update, precisa do ID também
      if include_id:
          emp_id = self.id_entry.get().strip()
          if not emp_id.isdigit():
              messagebox.showerror("Error", "ID must be a number for update.")
              return None
          emp.id = int(emp_id)

      return emp