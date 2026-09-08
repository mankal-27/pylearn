# Chained Assignment With a Mutable Object

inbox = None
review = None
archive = None

# TODO: use inbox = review = []
inbox = review = []
# TODO: use archive = []
archive = []
# TODO: append "draft" through inbox
inbox.append("draft")
# TODO: append "approved" through review
review.append("approved")
# TODO: append "saved" through archive
archive.append("saved")
# TODO: rebind review with review + ["sent"]

review += ["sent"]

print(f"inbox: {inbox}")
print(f"review: {review}")
print(f"archive: {archive}")
print(f"inbox is review: {inbox is review}")
print(f"inbox is archive: {inbox is archive}")