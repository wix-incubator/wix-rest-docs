SortOrder: 0
# Introduction

Member-to-Member Blocks enables `member A` to block `member B` and no longer see anything related to `member B`, except in a page displaying blocked member list, where `member A` could see and unblock `member B`, and see all their stuff again.

After `member A` blocks `member B`, `member B` no longer sees anything related to `member A`. Also, `member B` is not notified about creation of this block and cannot remove it.

## Limitations

 - No block-backs: `member A` cannot block `member B` if `member B` has already blocked `member A`.
 - No admin blocks: `member A` cannot block `member B` if `member A` and/or `member B` is an admin (a site owner or a contributor).
 - No self-blocks: `member A` cannot block `member A`.
 - No back-unblocks: after `member A` blocks `member B`, `member B` will not be able to remove `member A`'s incoming block.
