import ansible.runner
import ansible.playbook
import ansible.inventory
from ansible import callbacks
from ansible import utils
runner = ansible.runner.Runner(
   module_name='command',
   module_args='uptime',
   pattern='misa',
   forks=10
)

datastructure = runner.run()
print datastructure

stats = callbacks.AggregateStats()
playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)
pb = ansible.playbook.PlayBook(
        playbook = "/dj_pro/ansible-pro/play.yml",
        stats = stats,
        callbacks = playbook_cb,
        runner_callbacks = runner_cb
        )

result = pb.run()

print result
