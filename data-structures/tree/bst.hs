data (Ord k) => Tree k v = Empty | Node k v (Tree k v) (Tree k v) deriving Show

insert_bst :: (Ord k) => Tree k v -> k -> v -> Tree k v
insert_bst Empty k v = Node k v Empty Empty
insert_bst (Node k v l r) ik iv
	| ik == k = Node ik iv l r
	| ik <= k = Node k v (insert_bst l ik iv) r
	| ik > k = Node k v l (insert_bst r ik iv)


