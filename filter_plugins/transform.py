import json
import yaml

class FilterModule(object):
    def filters(self):
        return {
            'transform_deployment_config': self.transform_deployment_config
        }

    def transform_deployment_config(self, yaml_content):
        deploymentconfig = list(yaml.load_all(yaml_content, Loader=yaml.SafeLoader))

        if deploymentconfig[-1] is None:
            del deploymentconfig[-1]

        for manifest in deploymentconfig:
            if manifest and manifest['kind'] == 'DeploymentConfig':
                manifest['kind'] = 'Deployment'
                manifest['apiVersion'] = 'apps/v1'

                try:
                    manifest['spec']['strategy']['type'] = 'RollingUpdate'
                except:
                    pass

                try:
                    selector = json.dumps(manifest['spec']['selector'])
                    matchLabels = json.loads(selector)
                    manifest['spec']['selector']['matchLabels'] = matchLabels
                    for label in matchLabels:
                        del manifest['spec']['selector'][label]
                except:
                    pass

                try:
                    del manifest['spec']['strategy']['rollingParams']['intervalSeconds']
                except:
                    pass

                try:
                    del manifest['spec']['strategy']['rollingParams']['updatePeriodSeconds']
                except:
                    pass

                try:
                    rollingParams = json.dumps(manifest['spec']['strategy']['rollingParams'])
                    rollingUpdate = json.loads(rollingParams)
                    manifest['spec']['strategy']['rollingUpdate'] = rollingUpdate
                    del manifest['spec']['strategy']['rollingParams']
                except:
                    pass

                try:
                    del manifest['spec']['triggers']
                except:
                    pass

                try:
                    del manifest['spec']['test']
                except:
                    pass

                try:
                    del manifest['spec']['strategy']['activeDeadlineSeconds']
                except:
                    pass

                try:
                    del manifest['spec']['strategy']['resources']
                except:
                    pass

                try:
                    del manifest['metadata']['managedFields']
                except:
                    pass

                try:
                    del manifest['status']
                except:
                    pass

        return yaml.dump_all(deploymentconfig, default_flow_style=False)

