SortOrder: 0
# Bazel CI Police Service
Implements a translation layer between outputs produced by the Bazel `ci-police` rules and the `ci-police-station` service

## Architecture overview
Main service: BazelCIPoliceService - processes PR and Master builds and sends `ci-police` validation results to the `ci-police-station`

Secondary service: BazelCiPoliceLogService - provides a way to retrieve log file for `ci-police` target that was outputted
by the `bazel` rule

- In each commit to master:
  -  Bazel build pipeline runs all `ci-police` targets declared in build graph.
  - `BazelCIPoliceService.ConsumeBazelInvocationEvent` receives `BazelBuildInvocationEvent` event and reports `ci-police` targets results to `ci-police-station` service

- In each commit to PR:
  - Bazel build step runs all `ci-police` targets declared in build graph
  - CI Police build step informs sends HTTP request to `BazelCiPoliceService.CiPoliceCheck`
  - `BazelCIPoliceService` processes `ci-police` targets results and reports to `ci-police-station`
  - In case of `ci-police` rules failure - `BazelCIPoliceService` using `DevexUserNotifierClient` client creates comment with `ci-police` results
  - Results from the `ci-police-station` are reported back to the `Bazel CI` pipeline

### Validations
- only targets that will have `ci-police` will be processed
- bazel build needs to be successful to be able to retrieve results
- `ci-police` results must comply with [CI-Police rules](https://dev.wix.com/docs/rnd-general/devex/bazel-guides/bazel-ci-police/writing-new-rules)


## Links
[CI-Police Guides](https://dev.wix.com/docs/rnd-general/devex/bazel-guides/bazel-ci-police/intro)