import streamlit as st
from streamlit_mermaid import st_mermaid

# Page configuration
st.set_page_config(
    page_title="Git Branching Strategy Guide",
    page_icon="🌿",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #2E7D32;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #2E7D32;
        border-bottom: 2px solid #2E7D32;
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #E8F5E9;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E7D32;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🌿 Git Branching Strategy Guide</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">A beginner\'s guide to understanding Git branching strategies, including worktree and common approaches</div>', unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Common Branching Strategies",
    "🔧 Git Operations Guide",
    "🌳 Git Worktree",
    "📊 Comparison Table"
])

# Tab 1: Common Branching Strategies
with tab1:
    st.markdown('<h2 class="section-header">Common Branching Strategies</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <strong>Overview:</strong> Learn about the most popular Git branching strategies used in software development teams.
        Each strategy has its own strengths and is suited for different team sizes, workflows, and project requirements.
    </div>
    """, unsafe_allow_html=True)
    
    # Git Flow
    st.markdown("---")
    st.markdown("### 1. 🌊 Git Flow")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("""
        **Git Flow** is a robust branching model designed around project releases. It defines a strict branching 
        structure that's ideal for managing larger projects with scheduled release cycles.
        
        Created by Vincent Driessen, this model uses multiple long-lived branches and supports parallel development, 
        making it perfect for teams that need to maintain multiple versions of their software in production.
        """)
        
        st.markdown("**Key Branches:**")
        st.write("- 🎯 `main` - Production-ready code, always stable")
        st.write("- 🔧 `develop` - Integration branch where features come together")
        st.write("- ✨ `feature/*` - Individual feature development")
        st.write("- 🚀 `release/*` - Release preparation and final testing")
        st.write("- 🚨 `hotfix/*` - Emergency production fixes")
    
    with col2:
        st.markdown("**✅ Pros:**")
        st.write("- Clear separation of concerns")
        st.write("- Easy to maintain multiple versions")
        st.write("- Structured release process")
        st.write("- Parallel development support")
        
        st.markdown("**❌ Cons:**")
        st.write("- Complex for beginners")
        st.write("- Overhead for simple projects")
        st.write("- Slower release cycles")
        st.write("- Many branches to manage")
    
    st.markdown("**📊 Visual Workflow:**")
    git_flow_diagram = """
    gitGraph
        commit id: "Initial"
        branch develop
        checkout develop
        commit id: "Setup"
        
        branch feature/login
        checkout feature/login
        commit id: "Add login form"
        commit id: "Add validation"
        checkout develop
        merge feature/login
        
        branch feature/dashboard
        checkout feature/dashboard
        commit id: "Create dashboard"
        checkout develop
        merge feature/dashboard
        
        branch release/1.0
        checkout release/1.0
        commit id: "Version bump"
        commit id: "Bug fixes"
        checkout main
        merge release/1.0 tag: "v1.0"
        checkout develop
        merge release/1.0
        
        checkout main
        branch hotfix/critical
        commit id: "Fix security bug"
        checkout main
        merge hotfix/critical tag: "v1.0.1"
        checkout develop
        merge hotfix/critical
    """
    st_mermaid(git_flow_diagram, height=400)
    
    # GitHub Flow
    st.markdown("---")
    st.markdown("### 2. 🐙 GitHub Flow")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("""
        **GitHub Flow** is a lightweight, branch-based workflow that supports teams practicing continuous deployment. 
        It's simpler than Git Flow and focuses on keeping the main branch always deployable.
        
        Perfect for web applications and projects where you deploy frequently. The workflow is straightforward: 
        create a branch, add commits, open a pull request, discuss and review, deploy for testing, and merge.
        """)
        
        st.markdown("**Key Branches:**")
        st.write("- 🎯 `main` - Always deployable, production code")
        st.write("- ✨ `feature/*` - Short-lived feature branches")
        
        st.markdown("**Workflow Steps:**")
        st.write("1. Create a branch from `main`")
        st.write("2. Add commits with your changes")
        st.write("3. Open a pull request")
        st.write("4. Discuss and review code")
        st.write("5. Deploy and test")
        st.write("6. Merge to `main`")
    
    with col2:
        st.markdown("**✅ Pros:**")
        st.write("- Simple and easy to learn")
        st.write("- Fast deployment cycle")
        st.write("- Ideal for continuous delivery")
        st.write("- Minimal overhead")
        
        st.markdown("**❌ Cons:**")
        st.write("- Not ideal for scheduled releases")
        st.write("- Harder with multiple versions")
        st.write("- Requires good CI/CD")
        st.write("- Less structure for large teams")
    
    st.markdown("**📊 Visual Workflow:**")
    github_flow_diagram = """
    gitGraph
        commit id: "Initial"
        commit id: "Setup project"
        
        branch feature/user-auth
        checkout feature/user-auth
        commit id: "Add login"
        commit id: "Add signup"
        commit id: "Add tests"
        checkout main
        merge feature/user-auth tag: "Deploy v1.1"
        
        branch feature/payment
        checkout feature/payment
        commit id: "Add payment"
        commit id: "Add validation"
        checkout main
        merge feature/payment tag: "Deploy v1.2"
        
        branch fix/bug-123
        checkout fix/bug-123
        commit id: "Fix checkout bug"
        checkout main
        merge fix/bug-123 tag: "Deploy v1.2.1"
    """
    st_mermaid(github_flow_diagram, height=350)
    
    # GitLab Flow
    st.markdown("---")
    st.markdown("### 3. 🦊 GitLab Flow")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("""
        **GitLab Flow** combines feature-driven development with environment branches. It's a middle ground 
        between Git Flow and GitHub Flow, adding environment branches for staging and production.
        
        This strategy works well for teams that need both continuous deployment and the ability to maintain 
        different environments. It adds environment-specific branches (staging, production) while keeping 
        the simplicity of feature branches.
        """)
        
        st.markdown("**Key Branches:**")
        st.write("- 🎯 `main` - Latest development code")
        st.write("- 🎭 `staging` - Pre-production testing")
        st.write("- 🚀 `production` - Live production code")
        st.write("- ✨ `feature/*` - Feature development")
        
        st.markdown("**Key Principles:**")
        st.write("- Feature branches merge to `main`")
        st.write("- `main` promotes to `staging` for testing")
        st.write("- `staging` promotes to `production` when stable")
        st.write("- Supports multiple environments")
    
    with col2:
        st.markdown("**✅ Pros:**")
        st.write("- Clear environment progression")
        st.write("- Simpler than Git Flow")
        st.write("- Good for staged deployments")
        st.write("- Flexible for different needs")
        
        st.markdown("**❌ Cons:**")
        st.write("- More complex than GitHub Flow")
        st.write("- Requires environment management")
        st.write("- Can have merge conflicts")
        st.write("- Need good CI/CD pipeline")
    
    st.markdown("**📊 Visual Workflow:**")
    gitlab_flow_diagram = """
    gitGraph
        commit id: "Initial"
        branch staging
        branch production
        checkout main
        commit id: "Setup"
        
        branch feature/api
        checkout feature/api
        commit id: "Create API"
        commit id: "Add endpoints"
        checkout main
        merge feature/api
        
        branch feature/ui
        checkout feature/ui
        commit id: "Build UI"
        checkout main
        merge feature/ui
        
        checkout staging
        merge main
        commit id: "Staging tests pass"
        
        checkout production
        merge staging tag: "v1.0"
        
        checkout main
        branch feature/analytics
        commit id: "Add analytics"
        checkout main
        merge feature/analytics
        
        checkout staging
        merge main
        checkout production
        merge staging tag: "v1.1"
    """
    st_mermaid(gitlab_flow_diagram, height=400)
    
    # Trunk-Based Development
    st.markdown("---")
    st.markdown("### 4. 🌳 Trunk-Based Development")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("""
        **Trunk-Based Development** is a branching model where developers collaborate on a single branch called 
        'trunk' (usually `main`). Feature branches are very short-lived (hours, not days) and are integrated frequently.
        
        This approach is favored by high-performing engineering teams and is essential for true continuous integration. 
        It requires excellent testing practices, feature flags, and a mature CI/CD pipeline. Teams using this approach 
        typically commit to main multiple times per day.
        """)
        
        st.markdown("**Key Characteristics:**")
        st.write("- 🎯 Single `main` branch (the trunk)")
        st.write("- ⚡ Very short-lived feature branches (< 1 day)")
        st.write("- 🔄 Frequent integration (multiple times/day)")
        st.write("- 🚩 Feature flags for incomplete features")
        st.write("- ✅ Strong emphasis on automated testing")
        st.write("- 🚀 Release from main or release branches")
    
    with col2:
        st.markdown("**✅ Pros:**")
        st.write("- Minimal merge conflicts")
        st.write("- True continuous integration")
        st.write("- Fast feedback loops")
        st.write("- Simplified workflow")
        
        st.markdown("**❌ Cons:**")
        st.write("- Requires mature testing")
        st.write("- Need feature flags")
        st.write("- Requires team discipline")
        st.write("- Not for all team sizes")
    
    st.markdown("**📊 Visual Workflow:**")
    trunk_based_diagram = """
    gitGraph
        commit id: "Initial"
        commit id: "Setup CI/CD"
        
        branch feature-a
        checkout feature-a
        commit id: "Quick feature A"
        checkout main
        merge feature-a
        commit id: "Feature flag: A=on" tag: "v1.1"
        
        branch feature-b
        checkout feature-b
        commit id: "Quick feature B"
        checkout main
        merge feature-b
        
        branch feature-c
        checkout feature-c
        commit id: "Quick feature C"
        checkout main
        merge feature-c
        commit id: "Feature flags: B,C=on" tag: "v1.2"
        
        commit id: "Refactoring"
        
        branch hotfix
        checkout hotfix
        commit id: "Critical fix"
        checkout main
        merge hotfix tag: "v1.2.1"
    """
    st_mermaid(trunk_based_diagram, height=350)
    
    # Summary
    st.markdown("---")
    st.markdown("### 🎯 Which Strategy Should You Choose?")
    
    st.markdown("""
    <div class="info-box">
        <strong>Quick Decision Guide:</strong>
        <ul>
            <li><strong>Large project with scheduled releases?</strong> → Git Flow</li>
            <li><strong>Web app with continuous deployment?</strong> → GitHub Flow</li>
            <li><strong>Need staging and production environments?</strong> → GitLab Flow</li>
            <li><strong>Mature team with excellent CI/CD?</strong> → Trunk-Based Development</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Tab 2: Git Operations Guide
with tab2:
    st.markdown('<h2 class="section-header">Git Operations Guide</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <strong>Overview:</strong> Essential Git commands and operations for working with branches.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Creating Branches")
        st.code("""
# Create a new branch
git branch feature/new-feature

# Create and switch to new branch
git checkout -b feature/new-feature

# Or using newer syntax
git switch -c feature/new-feature
        """, language="bash")
        
        st.markdown("### Switching Branches")
        st.code("""
# Switch to existing branch
git checkout main

# Or using newer syntax
git switch main
        """, language="bash")
    
    with col2:
        st.markdown("### Merging Branches")
        st.code("""
# Merge feature branch into current branch
git merge feature/new-feature

# Merge with no fast-forward
git merge --no-ff feature/new-feature
        """, language="bash")
        
        st.markdown("### Deleting Branches")
        st.code("""
# Delete local branch
git branch -d feature/old-feature

# Force delete
git branch -D feature/old-feature

# Delete remote branch
git push origin --delete feature/old-feature
        """, language="bash")
    
    st.markdown("### Viewing Branches")
    st.code("""
# List local branches
git branch

# List all branches (local and remote)
git branch -a

# List remote branches
git branch -r
    """, language="bash")

# Tab 3: Git Worktree
with tab3:
    st.markdown('<h2 class="section-header">Git Worktree</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <strong>Overview:</strong> Git worktree allows you to check out multiple branches at once in different directories.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### What is Git Worktree?")
    st.write("""
    Git worktree is a powerful feature that allows you to have multiple working directories 
    associated with a single repository. This is useful when you need to work on multiple 
    branches simultaneously without constantly switching between them.
    """)
    
    st.markdown("### Benefits")
    st.write("✅ Work on multiple branches simultaneously")
    st.write("✅ No need to stash changes when switching contexts")
    st.write("✅ Faster context switching")
    st.write("✅ Each worktree has its own working directory")
    
    st.markdown("### Common Commands")
    st.code("""
# Add a new worktree
git worktree add ../feature-branch feature/new-feature

# List all worktrees
git worktree list

# Remove a worktree
git worktree remove ../feature-branch

# Prune deleted worktrees
git worktree prune
    """, language="bash")
    
    st.markdown("### Use Cases")
    st.write("""
    - **Emergency hotfixes:** Keep your feature branch while working on urgent fixes
    - **Code review:** Check out PR branches without disrupting your current work
    - **Testing:** Run tests on multiple branches simultaneously
    - **Comparison:** Compare implementations side by side
    """)

# Tab 4: Comparison Table
with tab4:
    st.markdown('<h2 class="section-header">Comparison Table</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <strong>Overview:</strong> Compare different branching strategies to find the best fit for your team.
    </div>
    """, unsafe_allow_html=True)
    
    # Branching strategies comparison
    st.markdown("### Branching Strategies Comparison")
    
    comparison_data = {
        "Strategy": ["Git Flow", "GitHub Flow", "Trunk-Based Development"],
        "Complexity": ["High", "Low", "Very Low"],
        "Best For": [
            "Large projects with scheduled releases",
            "Continuous deployment, web apps",
            "High-performing teams, CD/CI"
        ],
        "Release Cycle": ["Scheduled releases", "Continuous deployment", "Continuous deployment"],
        "Branch Lifetime": ["Long-lived", "Short-lived", "Very short-lived"],
        "Learning Curve": ["Steep", "Gentle", "Gentle"],
        "Team Size": ["Large teams", "Small to medium", "Any size"]
    }
    
    st.table(comparison_data)
    
    st.markdown("### Git Operations Comparison")
    
    operations_data = {
        "Operation": ["Branch Switching", "Working on Multiple Branches", "Disk Space", "Setup Complexity"],
        "Traditional Branching": ["Fast (git checkout)", "Requires stashing/committing", "Minimal", "Simple"],
        "Git Worktree": ["Instant (cd to directory)", "Native support", "Higher (multiple copies)", "Moderate"]
    }
    
    st.table(operations_data)
    
    st.markdown("### When to Use What?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Use Git Flow when:**")
        st.write("- You have scheduled releases")
        st.write("- Multiple versions in production")
        st.write("- Large team with clear roles")
        st.write("- Need strict release process")
    
    with col2:
        st.markdown("**Use GitHub Flow when:**")
        st.write("- Continuous deployment")
        st.write("- Web applications")
        st.write("- Small to medium teams")
        st.write("- Fast iteration needed")
    
    with col3:
        st.markdown("**Use Trunk-Based when:**")
        st.write("- Mature CI/CD pipeline")
        st.write("- High-performing teams")
        st.write("- Need rapid releases")
        st.write("- Good test coverage")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    Made with ❤️ for Git beginners | Learn more at 
    <a href="https://git-scm.com/doc" target="_blank">Git Documentation</a>
</div>
""", unsafe_allow_html=True)
