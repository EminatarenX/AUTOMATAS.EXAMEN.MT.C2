import tkinter as tk
from tkinter import ttk
import string

class TuringMachine:
    def __init__(self, states, alphabet, transition_function, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.final_states = final_states

    def process(self, text):
        current_state = self.start_state
        buffer = ""
        valid_strings = []

        for char in text:
            if char in self.alphabet:
                if current_state in self.transition_function and char in self.transition_function[current_state]:
                    current_state = self.transition_function[current_state][char]
                    buffer += char
                else:
                    if current_state in self.final_states:
                        valid_strings.append(buffer.strip())
                    current_state = self.start_state
                    buffer = ""
                    if char in self.transition_function[self.start_state]:
                        current_state = self.transition_function[self.start_state][char]
                        buffer = char
            else:
                if current_state in self.final_states:
                    valid_strings.append(buffer.strip())
                current_state = self.start_state
                buffer = ""

        if current_state in self.final_states:
            valid_strings.append(buffer.strip())

        return valid_strings

def setup_dfa():
    states = [
        'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
        'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
        'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
        'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q39', 'q40', 'q42',
        'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 'q52',
        'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60', 'q61', 'q62',
        'q63', 'q64', 'q65', 'q66', 'q67' ,'q68', 'q69', 'q70', 'q71', 'q72', 'q73', 'q74', 'q75'
    ]
    alphabet = set(string.ascii_uppercase + ' ')
    transition_function = {
        'q0': {'A': 'q1'},
        'q1': {'N': 'q2', 'C': 'q18', ' ': 'q36'},
        'q2': {'I': 'q3'},
        'q3': {'T': 'q4'},
        'q4': {'A': 'q5'},
        'q5': {' ': 'q6'},
        'q6': {'L': 'q7'},
        'q7': {'A': 'q8'},
        'q8': {'V': 'q9'},
        'q9': {'A': 'q10'},
        'q10': {' ': 'q11'},
        'q11': {'L': 'q12'},
        'q12': {'A': 'q13'},
        'q13': {' ': 'q14'},
        'q14': {'T': 'q15'},
        'q15': {'I': 'q16'},
        'q16': {'N': 'q17'},
        'q17': {'A': 'q18'},
        'q18':  {'A': 'q19'},
        'q19': {'S': 'q20'},
        'q20': {'O': 'q21'},
        'q21': {' ': 'q22'},
        'q22': {'H': 'q23'},
        'q23': {'U': 'q24'},
        'q24': {'B': 'q25'},
        'q25': {'O': 'q26'},
        'q26': {' ': 'q27'},
        'q27': {'B': 'q28'},
        'q28': {'U': 'q29'},
        'q29': {'H': 'q30'},
        'q30': {'O': 'q31'},
        'q31': {'S': 'q32'},
        'q32': {' ': 'q33'},
        'q33': {'A': 'q34'},
        'q34': {'C': 'q35'},
        'q35': {'A': 'q36'},
        # A cavar a caravaca
        'q36': {' ': 'q37'},
        'q37': {'A': 'q38'},
        'q38': {' ': 'q39'},
        'q39': {'C': 'q40'},
        'q40': {'A': 'q41'},
        'q41': {'V': 'q42'},
        'q42': {'A': 'q43'},
        'q43': {'R': 'q44'},
        'q44': {' ': 'q45'},
        'q45': {'A': 'q46'},
        'q46': {' ': 'q47'},
        'q47': {'C': 'q48'},
        'q48': {'A': 'q49'},
        'q49': {'R': 'q50'},
        'q50': {'A': 'q51'},
        'q51': {'V': 'q52'},
        'q52': {'A': 'q53'},
        'q53': {'C': 'q54'},
        'q54': {'A': 'q55'},
        
        # A colima va mi loca

        
    }
    start_state = 'q0'
    final_states = ['q18', 'q36', 'q55', 'q75']

    return TuringMachine(states, alphabet, transition_function, start_state, final_states)

class WordValidatorGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Evaluador de Palabras - Máquina de Turing")
        self.geometry("600x400")
        self.turing_machine = setup_dfa()

        # Configuración del estilo
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)

        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Frame para entrada y botones
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=0, column=0, pady=10, sticky=(tk.W, tk.E))

        # Etiqueta y campo de entrada
        ttk.Label(input_frame, text="Palabra:").grid(row=0, column=0, padx=5)
        self.word_entry = ttk.Entry(input_frame, width=30)
        self.word_entry.grid(row=0, column=1, padx=5)

        # Botones
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=0, column=2, padx=5)

        self.eval_button = ttk.Button(button_frame, text="Evaluar", command=self.evaluate_word)
        self.eval_button.grid(row=0, column=0, padx=2)

        self.clear_button = ttk.Button(button_frame, text="Limpiar Tabla", command=self.clear_table)
        self.clear_button.grid(row=0, column=1, padx=2)

        # Tabla de resultados
        self.create_table(main_frame)

        # Configurar expansión de widgets
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        input_frame.columnconfigure(1, weight=1)

    def create_table(self, parent):
        table_frame = ttk.Frame(parent)
        table_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        columns = ('palabra', 'resultado')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=10)

        self.tree.heading('palabra', text='Palabra')
        self.tree.heading('resultado', text='¿Palabra válida?')

        self.tree.column('palabra', width=200, anchor='center')
        self.tree.column('resultado', width=200, anchor='center')

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

    def evaluate_word(self):
        word = self.word_entry.get().strip().upper()
        valid_strings = self.turing_machine.process(word)
        is_valid = len(valid_strings) > 0
        self.tree.insert('', 'end', values=(word, 'Válida' if is_valid else 'No válida'))
        self.word_entry.delete(0, tk.END)

    def clear_table(self):
        self.tree.delete(*self.tree.get_children())

if __name__ == "__main__":
    app = WordValidatorGUI()
    app.mainloop()