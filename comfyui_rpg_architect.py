import json
import os

class rpgarchitect:
    @classmethod
    def INPUT_TYPES(cls):
        # Load options from JSON file
        options = cls.load_options()
        return {
            "optional": {
                "prompt": ("STRING", {"multiline": True}),
                "Gender_Age": (list(options["Gender_Age"].keys()),),
                "Race": (list(options["Race"].keys()),),
                "Character_class": (list(options["Character_class"].keys()),),
                "Armor": (list(options["Armor"].keys()),),
                "Action": (list(options["Action"].keys()),),
                "Environment": (list(options["Environment"].keys()),)
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Prompter"

    @staticmethod
    def load_options():
        # Load the JSON file containing the options and prompts
        json_path = os.path.join(os.path.dirname(__file__), "rpg_options.json")
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Options file not found: {json_path}")

        with open(json_path, 'r') as file:
            return json.load(file)

    def generate_prompt(self, prompt=None, Gender_Age=None, Race=None, Character_class=None, Armor=None, Action=None, Environment=None):
        options = self.load_options()

        # Use provided options or default to 'None' if not specified
        Gender_Age = Gender_Age or "None"
        Race = Race or "None"
        Character_class = Character_class or "None"
        Armor = Armor or "None"
        Action = Action or "None"
        Environment = Environment or "None"

        # Concatenate the prompts for each selected option
        prompt_parts = [
            part for part in [
                prompt if prompt else "",
                options["Gender_Age"].get(Gender_Age, ""),
                options["Race"].get(Race, ""),
                options["Character_class"].get(Character_class, ""),
                options["Armor"].get(Armor, ""),
                options["Action"].get(Action, ""),
                options["Environment"].get(Environment, "")
            ] if part and part.strip()
        ]
        
        # Join the prompt parts with periods
        final_prompt = ". ".join(prompt_parts)
        
        return ("24K UHD Photograph of " + final_prompt,)

# Node class mappings
NODE_CLASS_MAPPINGS = {
    "ComfyUI Rpg Architect 🪄": rpgarchitect
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI Rpg Architect 🪄": "ComfyUI Rpg Architect"
}
