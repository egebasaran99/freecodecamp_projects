def add_setting(settings, pair):
    """Add a new setting to the settings dictionary."""

    # Convert both the setting name and value to lowercase
    key = pair[0].lower()
    value = pair[1].lower()

    # Prevent adding a setting that already exists
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    # Add the new key-value pair to the dictionary
    settings[key] = value

    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, pair):
    """Update the value of an existing setting."""

    # Convert both the setting name and value to lowercase
    key = pair[0].lower()
    value = pair[1].lower()

    # Update the setting only if it already exists
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    # Return an error message if the setting does not exist
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    """Delete an existing setting from the settings dictionary."""

    # Convert the setting name to lowercase for consistency
    key = key.lower()

    # Delete the setting if it exists
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    # Return an error message if the setting cannot be found
    return "Setting not found!"


def view_settings(settings):
    """Return all current user settings in a readable format."""

    # Handle the case where no settings are available
    if len(settings) == 0:
        return "No settings available."

    # Start building the formatted output
    output = "Current User Settings:\n"

    # Add each setting on a separate line
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"

    return output


# Sample user settings used for testing the functions
test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}
