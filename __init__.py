from gym.envs.registration import register

register(
    id = 'WaterTable-v0',
    entry_point = 'Tabular_Games.Water.WaterTabular:WaterEnvTab',
    max_episode_steps = 100,
)
