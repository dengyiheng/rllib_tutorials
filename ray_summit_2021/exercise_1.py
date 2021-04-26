import numpy as np

from environment import MultiAgentArena


if __name__ == "__main__":
    # 3.
    # Exercise No1:
    # =============
    # Write an "environment loop" using our `MultiAgentArena` class.
    # 1) Create an env object.
    # 2) `reset` it to get the first observation.
    # 3) `step` through the environment using a provided
    #    "Trainer.compute_action([obs])" method to compute action dicts
    #    (see below).
    # 4) When an episode is done, remember to `reset()` the env before the
    #    next call to `step()`.
    # Good luck! :)

    class Trainer(object):
        def compute_action(self, obs):
            return {
                "agent1": np.random.randint(4),
                "agent2": np.random.randint(4)
            }
    trainer = Trainer()
    # Debug this.
    #print(trainer.compute_action({"agent1": 0, "agent2": 1}))

    # 3.a)
    # Solution:
    env = MultiAgentArena(config={"width": 10, "height": 10})
    obs = env.reset()
    episode_reward = 0.0
    # Play through a single episode.
    done = False
    while not done:
        action = trainer.compute_action(obs)
        obs, reward, done, _ = env.step(action)
        episode_reward += reward
        if done["__all__"]:
            print(f"R={episode_reward}")
            obs = env.reset()
            episode_reward = 0.0
        # Optional:
        # env.render()