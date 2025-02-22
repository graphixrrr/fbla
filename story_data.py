STORY_DATA = {
    "start": {
        "description": "You wake up in your cramped sleeping pod aboard the starship 'Horizon'. Warning lights flash across the control panel, and through the viewport, you see an unknown celestial anomaly pulsing with ethereal energy.",
        "choices": [
            {
                "text": "Check the ship's computer for information",
                "next_scene": "computer_check"
            },
            {
                "text": "Look closer at the anomaly",
                "next_scene": "examine_anomaly"
            },
            {
                "text": "Try to contact mission control",
                "next_scene": "contact_control"
            }
        ]
    },
    "computer_check": {
        "description": "The ship's computer displays corrupted data, but you manage to make out something about a quantum displacement field. The ship's sensors indicate that you're no longer in your original space-time coordinates.",
        "choices": [
            {
                "text": "Run a diagnostic on the ship's systems",
                "next_scene": "run_diagnostic"
            },
            {
                "text": "Search the database for similar anomalies",
                "next_scene": "search_database"
            }
        ]
    },
    "run_diagnostic": {
        "description": "The diagnostic reveals multiple system failures. Life support is stable, but the navigation system is malfunctioning. Strange energy readings suggest the anomaly is affecting the ship's core systems.",
        "choices": [
            {
                "text": "Attempt to restart the navigation system",
                "next_scene": "restart_navigation"
            },
            {
                "text": "Divert power to shields",
                "next_scene": "power_shields"
            }
        ]
    },
    "power_shields": {
        "description": "You reroute power to the shield generators. The shield bubble shimmer with an iridescent glow as it interacts with the anomaly's energy field.",
        "choices": [
            {
                "text": "Analyze shield harmonics",
                "next_scene": "analyze_harmonics"
            },
            {
                "text": "Increase shield intensity",
                "next_scene": "increase_shields"
            }
        ]
    },
    "analyze_harmonics": {
        "description": "The shield harmonics reveal a fascinating pattern - the anomaly's energy signature is compatible with your shield frequency. This could be used to establish a stable connection.",
        "choices": [
            {
                "text": "Attempt to synchronize shields",
                "next_scene": "maintain_shields"
            },
            {
                "text": "Research the pattern further",
                "next_scene": "search_database"
            }
        ]
    },
    "increase_shields": {
        "description": "As you increase shield power, the energy field begins to resonate with the anomaly. The ship's systems stabilize, providing a protective bubble against the strange phenomena.",
        "choices": [
            {
                "text": "Use shields to probe the anomaly",
                "next_scene": "maintain_shields"
            },
            {
                "text": "Maintain defensive posture",
                "next_scene": "observe_civilization"
            }
        ]
    },
    "restart_navigation": {
        "description": "The navigation system reboots, but the quantum interference from the anomaly makes traditional stellar navigation impossible. However, you might be able to use the anomaly's own properties for guidance.",
        "choices": [
            {
                "text": "Calculate a safe trajectory",
                "next_scene": "maintain_shields"
            },
            {
                "text": "Search for alternative navigation methods",
                "next_scene": "search_database"
            }
        ]
    },
    "search_database": {
        "description": "You find an old research paper about theoretical 'cosmic bridges' - wormhole-like phenomena that could transport ships across vast distances. The description matches what you're seeing.",
        "choices": [
            {
                "text": "Study the paper's recommendations",
                "next_scene": "study_recommendations"
            },
            {
                "text": "Look for recorded incidents",
                "next_scene": "past_incidents"
            }
        ]
    },
    "examine_anomaly": {
        "description": "As you peer through the viewport, the anomaly pulses with increasing intensity. Your instruments detect massive energy fluctuations, and suddenly, a beam of light engulfs your ship.",
        "choices": [
            {
                "text": "Activate the shields",
                "next_scene": "shields_up"
            },
            {
                "text": "Try to move away",
                "next_scene": "evasive_maneuvers"
            }
        ]
    },
    "shields_up": {
        "description": "The shields crackle with energy as they interact with the anomaly's beam. The ship's interior is bathed in an otherworldly glow, and you feel a strange sensation of weightlessness.",
        "choices": [
            {
                "text": "Maintain shield position",
                "next_scene": "maintain_shields"
            },
            {
                "text": "Modify shield frequency",
                "next_scene": "modify_frequency"
            }
        ]
    },
    "maintain_shields": {
        "description": "The shields hold steady against the anomaly's energy. Gradually, the ship begins to phase through space-time, and you glimpse what appears to be an advanced civilization through the viewport.",
        "choices": [
            {
                "text": "Attempt to communicate with the civilization",
                "next_scene": "contact_civilization"
            },
            {
                "text": "Stay hidden and observe",
                "next_scene": "observe_civilization"
            }
        ]
    },
    "modify_frequency": {
        "description": "As you adjust the shield frequency, you discover a pattern in the anomaly's energy signature. With careful tuning, you might be able to establish a controlled connection.",
        "choices": [
            {
                "text": "Synchronize with the pattern",
                "next_scene": "synchronize_pattern"
            },
            {
                "text": "Break the connection",
                "next_scene": "break_connection"
            }
        ]
    },
    "evasive_maneuvers": {
        "description": "You engage the thrusters, but the ship responds sluggishly. The anomaly's pull is too strong, and you're being drawn closer. The hull creaks under the strain.",
        "choices": [
            {
                "text": "Full power to engines",
                "next_scene": "full_power"
            },
            {
                "text": "Attempt emergency jump",
                "next_scene": "emergency_jump"
            }
        ]
    },
    "contact_control": {
        "description": "Static fills the communication channels. Through the noise, you hear fragments of a distress signal from another ship. They seem to be trapped in a similar situation.",
        "choices": [
            {
                "text": "Try to locate the source of the signal",
                "next_scene": "locate_signal"
            },
            {
                "text": "Focus on your own situation",
                "next_scene": "computer_check"
            }
        ]
    },
    "locate_signal": {
        "description": "You triangulate the signal's origin. It's coming from what appears to be another vessel, caught in a similar anomaly but in a different phase of space-time.",
        "choices": [
            {
                "text": "Attempt to establish communication",
                "next_scene": "establish_comm"
            },
            {
                "text": "Analyze their situation",
                "next_scene": "analyze_situation"
            }
        ]
    },
    "contact_civilization": {
        "description": "Your attempt at communication is successful! The advanced civilization welcomes you, sharing their knowledge of the cosmos and offering to help you return home - though you could choose to stay and learn from them.",
        "choices": [
            {
                "text": "Accept their offer to return home",
                "next_scene": "return_home"
            },
            {
                "text": "Stay and learn their knowledge",
                "next_scene": "stay_learn"
            }
        ]
    },
    "observe_civilization": {
        "description": "From your hidden position, you witness incredible technological achievements and peaceful cooperation among different species. Your observations could be invaluable to humanity.",
        "choices": [
            {
                "text": "Record everything and prepare to return",
                "next_scene": "record_findings"
            },
            {
                "text": "Risk making contact",
                "next_scene": "contact_civilization"
            }
        ]
    },
    "return_home": {
        "description": "With the advanced civilization's help, you navigate safely back to Earth. Your incredible journey has expanded humanity's understanding of the cosmos, and your discoveries will shape the future of space exploration.",
        "choices": []
    },
    "stay_learn": {
        "description": "You choose to remain with the advanced civilization, becoming a bridge between two worlds. Your decision marks the beginning of a new chapter in human-alien relations and your own cosmic journey.",
        "choices": []
    },
    "record_findings": {
        "description": "Your detailed observations of the advanced civilization provide humanity with unprecedented insights into alien technology and culture, revolutionizing our understanding of the universe.",
        "choices": []
    },
    "game_over": {
        "description": "Your journey through space has come to an end. The decisions you made have led you here, forever changing the course of your cosmic odyssey.",
        "choices": []
    },
    "synchronize_pattern": {
        "description": "By synchronizing with the anomaly's pattern, you create a stable connection, allowing for safe passage through the quantum displacement field.",
        "choices": [
            {"text": "Proceed through the anomaly", "next_scene": "contact_civilization"},
            {"text": "Abort the synchronization", "next_scene": "maintain_shields"}
        ]
    },
    "break_connection": {
        "description": "You disrupt the connection with the anomaly, causing a surge of energy that damages the ship's systems.  You're left stranded in unknown space.",
        "choices": [
            {"text": "Attempt emergency repairs", "next_scene": "game_over"}
        ]
    },
    "full_power": {
        "description": "You push the engines to their limits, but the anomaly's pull is too strong. The ship sustains critical damage, leading to a catastrophic failure.",
        "choices": [
            {"text": "Accept your fate", "next_scene": "game_over"}
        ]
    },
    "emergency_jump": {
        "description": "You attempt an emergency jump to hyperspace, but the anomaly interferes, causing the jump drive to malfunction.  The ship is severely damaged.",
        "choices": [
            {"text": "Try to salvage the ship", "next_scene": "game_over"}
        ]
    },
    "establish_comm": {
        "description": "You establish communication with the other vessel. They share valuable information about navigating the anomaly, giving you a better chance of survival.",
        "choices": [
            {"text": "Follow their advice", "next_scene": "maintain_shields"},
            {"text": "Ignore their advice", "next_scene": "evasive_maneuvers"}
        ]
    },
    "analyze_situation":{
        "description": "You analyze the other vessel's situation. They seem to be in worse condition than you are, with failing life support systems. Do you offer help?",
        "choices":[
            {"text": "Offer assistance", "next_scene": "establish_comm"},
            {"text": "Prioritize your own survival", "next_scene": "maintain_shields"}
        ]
    },
    "study_recommendations": {
        "description": "After studying the paper's recommendations, you formulate a plan to use the anomaly's properties for navigation.  This could be risky, but it might be your only option.",
        "choices": [
            {"text": "Attempt the risky maneuver", "next_scene": "maintain_shields"},
            {"text": "Seek a safer alternative", "next_scene": "search_database"}
        ]
    },
    "past_incidents": {
        "description": "Reviewing past incidents reveals that similar anomalies have led to both catastrophic failures and unexpected discoveries. The information is inconclusive.",
        "choices": [
            {"text": "Proceed cautiously", "next_scene": "maintain_shields"},
            {"text": "Take a calculated risk", "next_scene": "evasive_maneuvers"}
        ]
    }
}