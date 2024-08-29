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
                "Gender_Age": (list(options["Gender_Age"].keys()),),  # Ensure consistent naming
                "Race": (list(options["Race"].keys()),),
                "Character_Class": (list(options["Character_Class"].keys()),),  # Corrected naming to match JSON
                "Armor": (list(options["Armor"].keys()),),
                "Action": (list(options["Action"].keys()),),
                "Environment": (list(options["Environment"].keys()),),
                "Creatures": (list(options["Creatures"].keys()),)
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Prompter"

    @staticmethod
    def load_options():
        # Load the JSON file containing the options and prompts
        json_path = os.path.join(os.path.dirname(__file__), "RPG_options.json")
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Options file not found: {json_path}")

        with open(json_path, 'r') as file:
            return json.load(file)

    def generate_prompt(self, prompt, Gender_Age, Race, Character_Class, Armor, Action, Environment, Creatures):
        options = self.load_options()
        
        # Concatenate the prompts for each selected option
        prompt_parts = [
            part for part in [
                prompt,
                options["Gender_Age"].get(Gender_Age, ""),  # Ensure consistent naming
                options["Race"].get(Race, ""),
                options["Character_Class"].get(Character_Class, ""),
                options["Armor"].get(Armor, ""),
                options["Action"].get(Action, ""),
                options["Environment"].get(Environment, ""),
                options["Creatures"].get(Creatures, "")
            ] if part.strip() != ""
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
